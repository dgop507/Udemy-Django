from django.conf.urls import url, include
from appTwo import views

urlpatterns = [
    url(r'^$', views.users, name='users'),
]
