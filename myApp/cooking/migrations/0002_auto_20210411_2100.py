# Generated by Django 3.1.6 on 2021-04-12 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='meal_type',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Dessert', 'Dessert'), ('Snack', 'Snack')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='region',
            field=models.CharField(choices=[('America', 'America'), ('Europe', 'Europe'), ('Africa', 'Africa'), ('Asia', 'Asia'), ('Australia', 'Australia')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='timeToCook',
            field=models.CharField(choices=[('1-30 minutes', '1-30 minutes'), ('31-60 minutes', '31-60 minutes'), ('61+ minutes', '61+ minutes')], default='', max_length=100),
        ),
    ]
