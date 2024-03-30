from django.db import models

# Create your models here.
class Mission(models.Model):
    name = models.CharField(max_length=128)
    mission = models.CharField(max_length=1024)
    