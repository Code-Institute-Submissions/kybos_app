from django.conf.urls import url
from payments.views import payment_check_out

urlpatterns = [
    url(r'^checkout/(?P<id>\d+)', payment_check_out, name='check_out')
]