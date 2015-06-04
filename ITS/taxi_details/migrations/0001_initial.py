# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaxiDetailPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('taxi_id', models.CharField(max_length=10)),
                ('aadhar_no', models.TextField()),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=6)),
            ],
        ),
    ]
