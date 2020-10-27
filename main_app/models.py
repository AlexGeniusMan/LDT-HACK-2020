from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Test(models.Model):
    name = models.CharField(_("task name"), max_length=30, blank=True)
    theory = models.CharField(_("theory content"), max_length=30, blank=True)
    Grade = models.ForeignKey('Grade', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(_("task name"), max_length=30, blank=True)
    theory = models.CharField(_("theory content"), max_length=30, blank=True)
    Grade = models.ForeignKey('Grade', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Sprint(models.Model):
    name = models.CharField(_("sprint name"), max_length=30, blank=True)
    Grade = models.ForeignKey('Grade', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(_("class name"), max_length=30, blank=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class User(AbstractUser):
    middle_name = models.CharField(_("middle name"), max_length=30, blank=True)

    #     # password = models.CharField(_('password'), max_length=128, default='Alpine12')
    #     username_validator = UnicodeUsernameValidator()
    #     username = models.CharField(
    #         _('username'),
    #         max_length=150,
    #         unique=True,
    #         help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    #         validators=[username_validator],
    #         error_messages={
    #             'unique': _("A user with that username already exists."),
    #         },
    #         default='Alpine12',
    #     )

    # teacher = 'Учитель'
    # student = 'Ученик'
    # permission_choices = [(teacher, 'Учитель'), (student, 'Ученик')]
    # permission = models.CharField('Status', choices=permission_choices, default='Ученик', max_length=255)

    # class Meta:
    #     abstract = True
        # verbose_name = 'Пользователь'
        # verbose_name_plural = 'Пользователи'

    # def set_password(self, raw_password='Alpine12'):
    #     print('AHALAY MAHALAY -------------------------------- ')
    #     self.password = make_password(raw_password)
    #     self._password = raw_password
    #
    # def save(self, *args, **kwargs):
    #     print('AHALAY MAHALAY -------------------------------- ')
    #     self.username = 'student_' + self.id
    #     # self.password = 'Alpine12'
    #     super(User, self).save(*args, **kwargs)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s %s' % (self.first_name, self.last_name, self.middle_name)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()


# class Teacher(User):
#     pass
#
#
# class Student(User):
#     pass
