from rest_framework import generics

from api.models import Product
from api.serializers import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    """
    View for retrieving the list of products and creating a new product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
