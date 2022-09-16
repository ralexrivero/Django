from django.http import HttpResponse


def greet(request):
    return HttpResponse('Hello World')


def bye(request):
    return HttpResponse('Good bye!')