# Generated by Django 2.2.7 on 2019-11-06 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonKeeper', '0009_auto_20191106_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='student',
            field=models.ManyToManyField(related_name='contacts', to='lessonKeeper.Student'),
        ),
    ]
