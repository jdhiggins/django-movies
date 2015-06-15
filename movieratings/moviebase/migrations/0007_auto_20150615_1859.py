# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviebase', '0006_auto_20150611_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('genre', models.CharField(null=True, choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ("Children's", "Children's"), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Film-Noir', 'Film-Noir'), ('Horror', 'Horror'), ('Musical', 'Musical'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='posted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='text_rating',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='moviebase.Genre'),
        ),
    ]
