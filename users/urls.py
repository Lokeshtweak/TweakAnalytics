from cryptography.x509 import name
from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^siva/$',views.siva, name='siva'),
    url(r'^time/$',views.today_is, name='time')
]