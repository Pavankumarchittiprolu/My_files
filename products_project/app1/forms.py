from django.forms import ModelForm
from app1.models import *

class ProductsForm(ModelForm):
    class Meta:
        model=Products
        fields='__all__'
