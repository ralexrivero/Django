from django.shortcuts import render

def inheritance(request):
    return render(request, 'inheritance.html', {})

def example(request):
    return render(request, 'example.html', {})

def other(request):
    return render(request, 'other.html', {})

def index(request):
    return render(request, 'index.html', {})
