# Generated by Django 3.1.6 on 2021-04-12 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0004_auto_20210411_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='timeToCook',
            new_name='time_to_cook',
        ),
    ]