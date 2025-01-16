from django.urls import path
from .views import main,page
urlpatterns=[
    path("",main,name="person"),
    path('html/',page,name='people')
]