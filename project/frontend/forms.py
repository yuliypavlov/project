from django import forms

from api.models import Product


class ProductForm(forms.ModelForm):
    """
    Form for creating a new product.
    """
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

    def clean_price(self):
        """
        Ensures that the price is a positive number.
        """
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price
