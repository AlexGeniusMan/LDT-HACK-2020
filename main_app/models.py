from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from multiselectfield import MultiSelectField


class Test(models.Model):
    question = models.TextField("Входные данные", blank=True)
    answer = models.TextField("Выходные данные", blank=True)
    task = models.ForeignKey('Task', verbose_name='Тест', on_delete=models.PROTECT, related_name='test')


class TaskDetail(models.Model):
    is_done = models.BooleanField(_('Статус'), default=False)
    students = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Учащийся', on_delete=models.CASCADE)
    task = models.ForeignKey('Task', verbose_name='Задание', on_delete=models.CASCADE, related_name='task_detail')
    last_code = models.TextField(_("Последний запущенный код"), blank=True)


LANGUAGES = (('python', 'Python'),
             ('cpp', 'C++'),
             ('java', 'Java'),
             ('c_sharp', 'C#'),
             ('pascal', 'Pascal'))


class Task(models.Model):
    name = models.CharField(_("Название задания"), max_length=64, blank=True)
    theory = models.TextField(_("Теоретическое введение"), blank=True)
    mission = models.TextField(_("Техническое задание"), max_length=64, blank=True)
    sprint = models.ForeignKey('Sprint', on_delete=models.CASCADE, related_name='tasks')
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Учащиеся', through=TaskDetail)
    languages = MultiSelectField(choices=LANGUAGES, default='python')

    def __str__(self):
        return self.name


class Sprint(models.Model):
    name = models.CharField(_("Название спринта"), max_length=64, blank=True)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE, verbose_name='Класс', related_name='sprints')

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(_("Название класса"), max_length=64, blank=True)
    grades = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Пользователи', related_name='grades')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def __str__(self):
        return self.name


class User(AbstractUser):
    middle_name = models.CharField(_("middle name"), max_length=64, blank=True)

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
