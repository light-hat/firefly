import os
from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from django.utils.translation import gettext_lazy as _


class ProfileManager(BaseUserManager):
    """
     Переопределение класса Manager для модели кастомного пользователя.
     """

    def create_user(self, username, email, password):
        """
        Создает и возвращает пользователя с паролем и именем.
        """

        if username is None:
            raise TypeError('Не указано имя пользователя.')

        if email is None:
            raise TypeError('Не указан e-mail адрес пользователя.')

        if password is None:
            raise TypeError('У пользователя должен быть пароль.')

        user = self.model(
            username=username, 
            email=self.normalize_email(email)
        )
            
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Создает и возвращает пользователя с привилегиями суперадмина.
        """

        if username is None:
            raise TypeError('Не указано имя администратора.')

        if email is None:
            raise TypeError('Не указан e-mail адрес администратора.')

        if password is None:
            raise TypeError('У администратора должен быть пароль.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        #user.is_staff = True
        user.save(using=self._db)

        return user


class Profile(AbstractBaseUser, PermissionsMixin):
    """
    Реализация модели кастомного пользователя.
    """

    username = models.CharField(
        db_index=True,
        max_length=255,
        unique=True
    )

    email = models.EmailField(
        max_length = 255,
        unique=True
    )

    password = models.CharField(_('password'), max_length=128)

    surname = models.CharField(
        "Фамилия", 
        max_length=64
    )

    name = models.CharField(
        "Имя", 
        max_length=64
    )

    patronymic = models.CharField(
        "Отчество", 
        max_length=64
    )

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    objects = ProfileManager()

    USERNAME_FIELD = 'username'

    class Meta:
        """
        Метаданные модели.
        """

        ordering = ['-id']
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"

    def __str__(self):
        """
        Строковое представление модели.
        """

        return self.username


class ArchiveFile(models.Model):
    """ Модель подразделения. """

    def path_to_directory(instance, filename):
        """ 
        Формирование файловой структуры.
        """

        return 'upload_files/{0}/{1}'.format(
            instance.profile.username,
            filename
        )

    def validate_filename(value):
        """
        Валидатор имени файла.
        """

        if value == None or \
                value == "":

            raise ValidationError(
                _('Имя файла не должно быть пустым.'),
                params={'value': value},
            )

        if True in [x in value for x in ['\\', '/', ':', '*', '?', '"', '<', '>', '|']]:

            raise ValidationError(
                _('Имя файла содержит недопустимые символы.'),
                params={'value': value},
            )

    name = models.CharField(
        "Название медиафайла", 
        max_length=64, 
        validators=[validate_filename]
    )

    profile = models.ForeignKey(
        Profile,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )

    upload_datetime = models.DateTimeField(
        auto_now_add=True
    )

    file = models.FileField(
        "Файл",
        upload_to=path_to_directory,
        #validators=[FileExtensionValidator([
        #    'png',
        #    'jpg',
        #    'jpeg',
        #])]
    )

    class Meta:
        """
        Метаданные модели.
        """

        ordering = ['-id']
        verbose_name_plural = "Файлы"
        verbose_name = "Файл"

    def __str__(self):
        """
        Строковое представление модели.
        """

        return self.name
