from django.urls import path
from .views import *

urlpatterns = [
    path('reirster/',reirster.as_view(),name='reirster'),
    path('login/',login.as_view(),name='login'),
    path('active/<active_code>',active_user,name='active'),
    path('home/',home,name='home')
]
