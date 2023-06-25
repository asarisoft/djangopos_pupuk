from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, null=True)
    full_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    mobile_number = models.CharField(max_length=15, unique=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='children'
    )
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'mobile_number'
    # REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()

    def save(self, reupdate=True, *args, **kwargs):
        exist_id = self.id
        super(CustomUser, self).save(*args, **kwargs)
        if not exist_id:
            self.username = self.mobile_number
            self.save()

    def __str__(self):
        return f"{self.full_name} - {self.mobile_number}"
    
    CustomUserManager