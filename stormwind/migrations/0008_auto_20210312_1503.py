# Generated by Django 2.2.17 on 2021-03-12 15:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stormwind', '0007_auto_20210312_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thread',
            name='category',
            field=models.CharField(max_length=155),
        ),
    ]
