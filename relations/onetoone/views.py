from django.shortcuts import render
from .models import Place, Restaurant

def create(request):
    # create elements
    place1 = Place(name='The Crown', address='Hector Miranda 2424')
    place1.save()

    restaurant1 = Restaurant(place=place1, number_of_employees=8)
    restaurant1.save()

    return render(request, 'onetoone/create.html', {'r1':restaurant1})
