# Generated by Django 2.2.17 on 2021-03-11 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stormwind', '0002_auto_20210310_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
        ),
    ]
