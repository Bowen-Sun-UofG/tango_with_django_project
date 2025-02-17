from django.shortcuts import render
from rango.models import Category, Page

def index(request):

    category_list = Category.objects.order_by('-views')[:5]

    context_dict = {'categories': category_list}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')

def show_category(request, category_name):
    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
    except Category.DoesNotExist:
        category = None
        pages = None

    context_dict = {'category': category, 'pages': pages}
    return render(request, 'rango/category.html', context=context_dict)

