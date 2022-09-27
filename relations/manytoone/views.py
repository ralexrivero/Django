from datetime import date
from django.shortcuts import render
from .models import Reporter, Article

def create(request):
    r1 = Reporter(first_name='Ronald', last_name='Rivero', email='ralexrivero@gmail.com')
    r1.save()
    a1 = Article(headline='Been a Full Stack Developer', pub_date=date.today(), reporter=r1)
    a1.save()

    return render(request, 'manytoone/create.html', {'a1':a1})
