# Generated by Django 2.2.3 on 2021-09-07 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ft_ba', '0008_auto_20210906_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_one',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_two',
        ),
    ]
