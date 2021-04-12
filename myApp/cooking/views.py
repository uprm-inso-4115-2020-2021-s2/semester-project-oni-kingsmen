from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from .forms import RecipeForm
from django.shortcuts import render, redirect
from .filters import RecipeFilter
from django.contrib.auth.models import User


# Create your views here.
# This class is for every 'path' in the cooking home page.
# The 'about' path can be deleted later, since we won't have an about section.
# The request parameter isn't used yet


def home(request):
    return render(request, 'cooking/home.html')


def about(request):
    return render(request, 'cooking/about.html', {'title': 'About'})


def addRecipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author_id = request.user.id
            form.save()
        return redirect("cooking-home")
    else:
        form = RecipeForm()
    return render(request, "cooking/addRecipe.html", {"form": form})


def myRecipes(request):
    my_recipes = Recipe.objects.filter(author=request.user)
    context = {'my_recipes': my_recipes}
    return render(request, 'cooking/myRecipes.html', context)


def search(request):
    recipes = Recipe.objects.all()
    myFilter = RecipeFilter(request.GET, queryset=recipes)
    recipes = myFilter.qs
    context = {'recipes': recipes, 'myFilter': myFilter}

    return render(request, 'cooking/search.html', context)
