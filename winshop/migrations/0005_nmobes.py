# Generated by Django 4.1.6 on 2023-03-04 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winshop', '0004_tap_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nmobes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.CharField(default=None, max_length=20, verbose_name='问句')),
                ('answer', models.CharField(default=None, max_length=20, verbose_name='答句')),
            ],
        ),
    ]
