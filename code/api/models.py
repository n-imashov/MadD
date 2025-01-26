from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    date_of_birth = models.DateField()
    diagnoses = models.JSONField()  # Используем JSONField для хранения списка
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Patient {self.id}"
