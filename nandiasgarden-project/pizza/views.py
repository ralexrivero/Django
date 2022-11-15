from django.shortcuts import render
# from django.views.generic import TemplateView, CreateView
from .forms import PizzaForm

""" class HomeView(TemplateView):
    template_name = 'pizza/home.html'


class OrderView(CreateView):
    form_class = PizzaForm
    template_name = 'pizza/order.html' """


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    form = PizzaForm()
    return render(request, 'pizza/order.html', {'pizzaform': form})
