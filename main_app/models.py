from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings


# class Test(models.Model):
#     name = models.CharField(_("task name"), max_length=30, blank=True)
#     theory = models.CharField(_("theory content"), max_length=30, blank=True)
#     Grade = models.ForeignKey('Grade', on_delete=models.PROTECT)
#
#     def __str__(self):
#         return self.name

class TaskDetail(models.Model):
    is_done = models.BooleanField(_('Статус'))
    students = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Учащийся', on_delete=models.PROTECT)
    task = models.ForeignKey('Task', verbose_name='Задание', on_delete=models.PROTECT, related_name='task_detail')
    last_code = models.CharField(_("Последний запущенный код"), max_length=300, blank=True)


class Task(models.Model):
    name = models.CharField(_("Название задания"), max_length=30, blank=True)
    theory = models.CharField(_("Теоретическое введение"), max_length=30, blank=True)
    mission = models.CharField(_("Техническое задание"), max_length=30, blank=True)
    sprint = models.ForeignKey('Sprint', on_delete=models.PROTECT, related_name='tasks')
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Учащиеся', through=TaskDetail)

    # языки

    def __str__(self):
        return self.name


class Sprint(models.Model):
    name = models.CharField(_("Название спринта"), max_length=30, blank=True)
    grade = models.ForeignKey('Grade', on_delete=models.PROTECT, verbose_name='Класс', related_name='sprints')

    class Meta:
        verbose_name = 'Спринт'
        verbose_name_plural = 'Спринты'

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(_("Название класса"), max_length=30, blank=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Пользователи')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def __str__(self):
        return self.name


class User(AbstractUser):
    middle_name = models.CharField(_("middle name"), max_length=30, blank=True)

    # teacher = 'Учитель'
    # student = 'Ученик'
    # status_choices = [(teacher, 'Учитель'), (student, 'Ученик')]
    # status = models.CharField('Status', choices=status_choices, default='Ученик', max_length=255)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_full_name(self):
        if self.groups.filter(name='Учителя').exists():
            admin_panel_name = 'УЧИТЕЛЬ | ' + self.email + ' (' + self.last_name + ' ' + self.first_name[
                                                                                         0:1] + '.' + self.middle_name[
                                                                                                      0:1] + '.)'
        elif self.groups.filter(name='Ученики').exists():
            admin_panel_name = '' + self.email + ' (' + self.last_name + ' ' + self.first_name[
                                                                               0:1] + '.' + self.middle_name[0:1] + '.)'
        else:
            admin_panel_name = 'none | ' + self.email + ' (' + self.last_name + ' ' + self.first_name[
                                                                                      0:1] + '.' + self.middle_name[
                                                                                                   0:1] + '.)'
        return admin_panel_name

    def __str__(self):
        return self.get_full_name()
