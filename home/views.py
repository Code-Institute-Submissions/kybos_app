from django.shortcuts import render
from products.models import Terrarium
# Create your views here.

def get_home(request):
    products = Terrarium.objects.all()
    return render(request, 'home.html', {'products':products})