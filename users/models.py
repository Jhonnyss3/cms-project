from datetime import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=150, blank=True, verbose_name='Nome Completo')
    email = models.EmailField(unique=True, verbose_name='Endereço de Email')
    photo = models.ImageField(upload_to='users/photos/%Y/%m/%d/', blank=True, null=True, verbose_name='Foto de Perfil')
    created_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['name', 'email']

    def __str__(self):
        return self.username