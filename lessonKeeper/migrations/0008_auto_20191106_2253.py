# Generated by Django 2.2.7 on 2019-11-06 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonKeeper', '0007_auto_20191106_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='student',
            field=models.ManyToManyField(default='', related_name='contacts', to='lessonKeeper.Student'),
        ),
    ]