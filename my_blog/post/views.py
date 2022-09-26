from django.shortcuts import render
from .models import Author, Entry

def queries(request):
    # get all the elements
    authors = Author.objects.all()

    # get filtered data
    filtered = Author.objects.filter(email='alexandra80@example.org')

    # get a single data using get
    author = Author.objects.get(id=1)  # return the __str__ method

    # limited query, first 10 records
    limits = Author.objects.all()[:10]

    # offset, get 5 records avoiding first 5 records
    offsets = Author.objects.all()[5:10]

    # order
    orders = Author.objects.all().order_by('email')

    # get records where ide is less or equal than 15
    filtered2 = Author.objects.filter(id__lte=15).order_by('email').filter(email__contains='rg').filter(email__startswith='a')

    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limits': limits, 'offsets': offsets, 'orders': orders, 'filtered2': filtered2})


def update(request):
    qu1 = Author.objects.get(id=1)
    qu1.name = 'Ronald'
    qu1.email = 'ralexrivero@gmail.com'
    qu1.save()

    return render(request, 'post/update.html', {'qu1': qu1})
