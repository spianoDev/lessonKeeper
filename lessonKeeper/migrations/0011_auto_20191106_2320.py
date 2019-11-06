# Generated by Django 2.2.7 on 2019-11-06 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonKeeper', '0010_auto_20191106_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=180),
        ),
        migrations.AlterField(
            model_name='student',
            name='lesson_time',
            field=models.TimeField(max_length=10),
        ),
    ]
