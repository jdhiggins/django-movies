# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import moviebase.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('moviebase', '0007_auto_20150615_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='posted_at',
            field=models.DateTimeField(null=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(validators=[moviebase.models.one_to_five], choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='text_rating',
            field=models.CharField(null=True, default='None', max_length=255),
        ),
    ]
