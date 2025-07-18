from django.urls import path
from .views import HomeView, ContactsView, ProductDetailView, ProductCreateView, ProductUpdateView

app_name = 'catalog'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('products/<int:product_id>/update', ProductUpdateView.as_view(), name='update'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='products'),
]
