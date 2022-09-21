from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inheritance/', views.inheritance, name='inheritance'),
    path('example/', views.example, name='example'),
    path('other/', views.other, name='other')
]
