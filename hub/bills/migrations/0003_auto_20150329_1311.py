# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_institutions(apps, schema_editor):
    Institution = apps.get_model('bills', 'Institution')
    Institution.objects.create(
        name="Ministerul Pentru Societatea Informațională",
        slug='msi',
    ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0002_institution_slug'),
    ]

    operations = [
        migrations.RunPython(create_institutions),
    ]
