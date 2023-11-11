from django.urls import path
from .views import *

urlpatterns = [
    path('reirster/',reirster.as_view(),name='reirster')
]
