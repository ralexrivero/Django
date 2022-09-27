from datetime import date
from django.shortcuts import render
from .models import Reporter, Article

def create(request):
    r1 = Reporter(first_name='Ronald', last_name='Rivero', email='ralexrivero@gmail.com')
    r1.save()
    a1 = Article(headline='Been a Full Stack Developer', pub_date=date.today(), reporter=r1)
    a1.save()
    a2 = Article(headline='DevOps Fundation', pub_date=date.today(), reporter=r1)
    a2.save()
    a3 = Article(headline='Backend Frameworks', pub_date=date.today(), reporter=r1)
    a3.save()

    # queries
    q1 = a1.reporter.first_name
    q2 = r1.article_set.all()
    q3 = r1.article_set.count()

    return render(request, 'manytoone/create.html', {'a1':a1, 'q1':q1, 'q2': q2, 'q3': q3})
