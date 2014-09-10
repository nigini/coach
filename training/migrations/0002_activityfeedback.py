# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=1000)),
                ('activity', models.ForeignKey(to='training.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
