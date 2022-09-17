from django.shortcuts import render

def simple(request):
    return render(request, 'simple.html', {})

def dynamic(request, name):
    categories = ['code', 'design', 'marketing']
    context = {'name': name, 'categories' : categories}
    return render(request, 'dynamic.html', context)
