from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse('Works!')


def create(request):
    return HttpResponse('Create')
