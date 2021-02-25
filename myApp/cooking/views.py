from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# This class is for every 'path' in the cooking home page.
# The 'about' path can be deleted later, since we won't have an about section.
# The request parameter isn't used yet

posts = [
    {
        'author': 'Christian Carrion',
        'title': 'First Recipe Posted',
        'content': 'Risotto de Churrasco',
        'date_posted': 'February 24, 2021',
    },
    {
        'author': 'Laura Delgado',
        'title': 'Second Recipe Posted',
        'content': 'Peanut Butter Chocolate Banana',
        'date_posted': 'February 25, 2021',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'cooking/home.html', context)


def about(request):
    return render(request, 'cooking/about.html', {'title': 'About'})
