from django.http import HttpResponse
from django.shortcuts import render
from .models import Comment


def test(request):
    return HttpResponse('Works!')


def create(request):
    comment = Comment(name='John',score=5, comment='This is a comment')
    comment.save()
    return HttpResponse(comment.signature)


def delete(request):
    comment = Comment.objects.first()
    if comment != None:
        return HttpResponse(comment.delete())
    else:
        return HttpResponse('Nothing to delete')