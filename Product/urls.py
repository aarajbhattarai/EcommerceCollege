from django.urls import path
from .views import ProductListView, ProductDetailView

app_name = 'Product'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('<slug:slug>', ProductDetailView.as_view(), name='detail'),

]
