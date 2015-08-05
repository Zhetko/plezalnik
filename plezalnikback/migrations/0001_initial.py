# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('achievement_type', models.CharField(max_length=20)),
                ('grade_no', models.IntegerField()),
                ('grade_letter', models.CharField(max_length=1)),
                ('grade_speed', models.CharField(max_length=20)),
                ('isfirst', models.BooleanField()),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fullname', models.CharField(max_length=200)),
                ('fb_id', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=75, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='achievement',
            name='user',
            field=models.ForeignKey(to='plezalnikback.User'),
            preserve_default=True,
        ),
    ]
