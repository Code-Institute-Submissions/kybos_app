from django.conf.urls import url
from products.views import product_detail


urlpatterns = [
    url(r'^(?P<id>\d+)$', product_detail, name='product_detail')
]