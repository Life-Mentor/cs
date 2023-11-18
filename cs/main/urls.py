from django.urls import path
from .views import *

urlpatterns = [
    path('',index.as_view(),name='index'),
    path('aboutus/',aboutus.as_view(),name='aboutus'),
    path('article/',overall.as_view(),name='article'),
    path('detailed/<int:detailed_id>',check.as_view(),name='detailed'),

    path('ce/',ce,name='ce')
]
