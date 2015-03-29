from django.db import models


class Institution(models.Model):
    name = models.CharField(max_length=1024)


class Bill(models.Model):
    key = models.CharField(max_length=1024)
    title = models.CharField(max_length=1024)
    url = models.URLField(max_length=1024)
    institution = models.ForeignKey(Institution)
