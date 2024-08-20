from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product


# Create your views here.
class ProductView(TemplateView):
    template_name = "product.html"
    def get_context_data(self, **kwargs):
        prds_obj=Product.objecta.all()
        context = {'product':prds_obj}
        return context