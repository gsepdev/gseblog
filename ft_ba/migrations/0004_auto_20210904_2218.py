# Generated by Django 2.2.3 on 2021-09-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ft_ba', '0003_auto_20210904_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_one',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_three',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_two',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
