from django.conf.urls import url
from basic_aoo import views
from django.urls import path

#TEMPLATE TAGGING
app_name = 'basic_aoo'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('path/', views.other, name='other'),
]
