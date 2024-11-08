from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from organization.models import Organization
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError

from PIL import Image

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValidationError('The Email field must be set')
        if not password:
            raise ValidationError('The Password field must be set')
        if password and len(password) > 128:
            raise ValidationError('Password is too long')
            
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    organizations = models.ManyToManyField(Organization, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    def __str__(self):
        return self.email
    def save(self, *args, **kwargs):

        # Изменение размера изображения
        if self.avatar:
            img = Image.open(self.avatar)
            img.thumbnail((200, 200))  # Изменяем размер до 200x200

            # Сохраняем изображение обратно в поле avatar
            # Сначала создаем буфер
            from io import BytesIO
            from django.core.files.base import ContentFile

            thumb_io = BytesIO()
            img.save(thumb_io, format='JPEG', quality=85) # Сохраняем изображение в буфер
            thumb_file = ContentFile(thumb_io.getvalue(), name=self.avatar.name)
            self.avatar.save(thumb_file.name, thumb_file, save=False)

        super().save(*args, **kwargs)
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
    def __str__(self):
        return self.email