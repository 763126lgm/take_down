# Generated by Django 4.1.6 on 2023-04-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winshop', '0007_alter_nmobes_answer_alter_nmobes_ask_mouth'),
    ]

    operations = [
        migrations.CreateModel(
            name='File_upl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=12, verbose_name='文件标题')),
                ('upload', models.FileField(upload_to='file_upload')),
            ],
        ),
    ]
