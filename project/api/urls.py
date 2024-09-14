from django.urls import path

from api.views import ProductListCreateView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(),
         name='product_list_create'),
]
