# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviebase', '0002_auto_20150609_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(null=True, choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ("Children's", "Children's"), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Film-Noir', 'Film-Noir'), ('Horror', 'Horror'), ('Musical', 'Musical'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], max_length=30),
        ),
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='rating',
            name='date_posted',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(null=True, to='moviebase.Movie'),
        ),
        migrations.AddField(
            model_name='rating',
            name='rater',
            field=models.ForeignKey(null=True, to='moviebase.Rater'),
        ),
        migrations.AddField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(null=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='rater',
            name='job',
            field=models.IntegerField(null=True, choices=[(0, 'other'), (1, 'academic/educator'), (2, 'artist'), (3, 'clerical/admin'), (4, 'college/grad student'), (5, 'customer service'), (6, 'doctor/health care'), (7, 'executive/managerial'), (8, 'farmer'), (9, 'homemaker'), (10, 'K-12 student'), (11, 'lawyer'), (12, 'programmer'), (13, 'retired'), (14, 'sales/marketing'), (15, 'scientist'), (16, 'self-employed'), (17, 'technician/engineer'), (18, 'tradesman/craftsman'), (19, 'unemployed'), (20, 'writer')], default=0),
        ),
    ]
