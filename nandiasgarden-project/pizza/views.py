from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'pizza/home.html'


class OrderView(TemplateView):
    template_name = 'pizza/order.html'


""" def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    return render(request, 'pizza/order.html') """
