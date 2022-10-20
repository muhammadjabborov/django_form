from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, DateTimeField, ImageField, CharField, EmailField


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Employer(BaseModel):
    image = ImageField(upload_to='profiles/')
    username = CharField(max_length=255)
    name = CharField(max_length=255)
    email = EmailField(max_length=255)
    company = CharField(max_length=255)


