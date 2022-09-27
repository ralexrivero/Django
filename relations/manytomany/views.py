from django.shortcuts import render
from .models import Publication, Article

def create(request):
    """
    pub1 = Publication(title='Title 1')
    pub1.save()
    pub2 = Publication(title='Title 2')
    pub2.save()
    pub3 = Publication(title='Title 3')
    pub3.save()
    pub4 = Publication(title='Title 4')
    pub4.save()

    art1 = Article(headline='Headline 1')
    art1.save()
    art2 = Article(headline='Headline 2')
    art2.save()
    art3 = Article(headline='Headline 3')
    art3.save()
    art4 = Article(headline='Headline 4')
    art4.save()
    art5 = Article(headline='Headline 5')
    art5.save()
    art6 = Article(headline='Headline 6')
    art6.save()
    art7 = Article(headline='Headline 7')
    art7.save()

    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)
    art2.publications.add(pub4)
    art2.publications.add(pub3)
    art3.publications.add(pub4)
    art5.publications.add(pub1)
    art6.publications.add(pub1)
    art7.publications.add(pub3)
    """
    art1 = Article.objects.get(id=1)

    q1 = art1.publications.all()
    q2 = art1.publications.count()

    pub1 = Publication.objects.get(id=1)
    q3 = pub1.article_set.all()

    art2 = Article.objects.get(id=2)
    pub4 = Publication.objects.get(id=4)
    art2.publications.remove(pub4)

    return render (request, 'manytomany/create.html', {'q1':q1, 'q2':q2, 'q3':q3})
