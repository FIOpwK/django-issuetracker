from django.db import models


# Create your models here.
class Issue(models.Model):
    text = models.TextField(default='')


