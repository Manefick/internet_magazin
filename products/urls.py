from django.urls import path
from . import views

urlpatterns = [
    path('<product_id>', views.product, name= 'product'),
]