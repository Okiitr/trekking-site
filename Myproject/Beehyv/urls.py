from django.contrib import admin
from django.urls import URLPattern, path,include
from.import views

urlpatterns = [
    path('', views.Index),
    path('index', views.Index),
    path('trekking', views.Generic),
    path('elements', views.Elements),
    path('contact', views.Contact),
    

    
]
