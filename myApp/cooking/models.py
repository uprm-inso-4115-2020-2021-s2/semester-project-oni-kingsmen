from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Recipe(models.Model):
    DIFFICULTY = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    ]

    TIME_TO_COOK = [
        ('1-30 minutes', '1-30 minutes'),
        ('31-60 minutes', '31-60 minutes'),
        ('61+ minutes', '61+ minutes'),
    ]

    REGION = [
        ('America', 'America'),
        ('Europe', 'Europe'),
        ('Africa', 'Africa'),
        ('Asia', 'Asia'),
        ('Australia', 'Australia')
    ]

    MEAL_TYPE = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Dessert', 'Dessert'),
        ('Snack', 'Snack'),
    ]

    title = models.CharField(max_length=100, null=True)
    difficulty = models.CharField(
        max_length=100,
        choices=DIFFICULTY,
        null=True
    )
    time_to_cook = models.CharField(
        max_length=100,
        choices=TIME_TO_COOK,
        null=True
    )
    region = models.CharField(
        max_length=100,
        choices=REGION,
        null=True
    )
    meal_type = models.CharField(
        max_length=100,
        choices=MEAL_TYPE,
        null=True
    )
    content = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_saved = models.BooleanField(default=False)

    # This method enables the data to be shown by recipe title
    def __str__(self):
        return self.title;
