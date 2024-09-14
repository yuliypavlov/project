from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from api.models import Product
from frontend.forms import ProductForm


class ProductListView(ListView):
    """
    View for getting a list of all products.
    """
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    """
    View for creating a new product.
    """
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('product_list')
