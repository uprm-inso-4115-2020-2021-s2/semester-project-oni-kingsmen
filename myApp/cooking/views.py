from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from .forms import RecipeForm
from django.shortcuts import render, redirect
from .filters import RecipeFilter


# Create your views here.
# This class is for every 'path' in the cooking home page.
# The 'about' path can be deleted later, since we won't have an about section.
# The request parameter isn't used yet


def home(request):
    return render(request, 'cooking/home.html')


def about(request):
    return render(request, 'cooking/about.html', {'title': 'About'})


# Create your views here.
def addRecipe(response):
    if response.method == "POST":
        form = RecipeForm(response.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author_id = response.user.id
            form.save()
        return redirect("cooking-home")
    else:
        form = RecipeForm()
    return render(response, "cooking/addRecipe.html", {"form": form})


def search(request):
    recipes = Recipe.objects.all()
    myFilter = RecipeFilter(request.GET, queryset=recipes)
    recipes = myFilter.qs
    context = {'recipes': recipes, 'myFilter': myFilter}

    return render(request, 'cooking/search.html', context)
