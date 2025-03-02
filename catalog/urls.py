from django.urls import path
from catalog.apps import CatalogConfig
from . import views

catalog_name = CatalogConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
]
