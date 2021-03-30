from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# The data-base of the application is built here

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # This method enables the data to be shown by recipe title
    def __str__(self):
        return self.title;
