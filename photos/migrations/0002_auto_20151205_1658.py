# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 12, 5, 7, 57, 15, 273547, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(max_length=500, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='', upload_to='%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 12, 5, 7, 57, 53, 87710, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
