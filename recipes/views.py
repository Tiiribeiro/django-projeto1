from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/index.html', context={
        'name': 'Luiz Otávio',
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe.html', context={
        'name': 'Luiz Otávio',
    })


def base(request):
    return render(request, 'global/base.html', context={
        'name': 'Luiz Otávio',
    })
