import django_filters

from .models import Recipe


class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ['title', 'date_posted', 'author']
