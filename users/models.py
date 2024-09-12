# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('User', 'User')
    )
    contact = models.CharField(unique=True, max_length=20)
    user_type = models.CharField(choices=USER_TYPE_CHOICES, default='User')

    def __str__(self):
        return f'User ID: {id}, Name: {self.first_name} {self.last_name}, Contact {self.contact}'
