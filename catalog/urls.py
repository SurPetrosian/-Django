from django.urls import path
from .views import HomeView, ContactsView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='products'),
]
