from django.forms import ModelForm
from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'difficulty', 'time_to_cook', 'region', 'meal_type', 'content']
