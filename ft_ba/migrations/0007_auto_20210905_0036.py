# Generated by Django 2.2.3 on 2021-09-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ft_ba', '0006_auto_20210905_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_two',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
