from django.shortcuts import render
from rango.models import Category

def index(request):
    categories = Category.objects.order_by('name')[:5]

    context_dict = {'categories': categories}

    return render(request, 'rango/index.html', context=context_dict)