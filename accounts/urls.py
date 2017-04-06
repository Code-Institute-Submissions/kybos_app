from django.conf.urls import url
from views import log_out, profile

urlpatterns = [
    url(r'^profile$', profile, name='profile'),
    url(r'^log_out$', log_out, name='log_out'),
]
