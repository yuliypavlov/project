from django.urls import path

from frontend.views import ProductListView, ProductCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
]
