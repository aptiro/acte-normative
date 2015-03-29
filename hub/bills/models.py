from django.db import models


class Institution(models.Model):
    name = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name


class Bill(models.Model):
    key = models.CharField(max_length=1024)
    title = models.CharField(max_length=1024)
    url = models.URLField(max_length=1024)
    institution = models.ForeignKey(Institution)

    def __unicode__(self):
        return u"{s.title} ({s.institution.name})".format(s=self)
