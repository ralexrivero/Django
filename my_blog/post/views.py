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

    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limits': limits})
