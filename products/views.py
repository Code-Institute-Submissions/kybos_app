from django.shortcuts import render, get_object_or_404
from products.models import Terrarium

# Create your views here.


def product_detail(request, id):
    product_details = get_object_or_404(Terrarium, pk=id)
    return render(request, 'product_detail.html', {'product_details': product_details})
