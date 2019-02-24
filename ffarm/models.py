from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    token = models.CharField(max_length=100)
    profile_picture = models.CharField(max_length=100)
