# Generated by Django 4.1.6 on 2023-02-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winshop', '0002_alter_tap_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='tap',
            name='stud_number',
            field=models.IntegerField(default='20180000', verbose_name='学号'),
        ),
    ]
