from django.urls import path
from .views import *

urlpatterns = [
    path('',index.as_view(),name='index'),
    path('aboutus/',aboutus.as_view(),name='aboutus'),
    path('article/',overall.as_view(),name='article'),
    path('detailed/<int:detailed_id>',check.as_view(),name='detailed'),
    path('submitbug/',SubmitBug.as_view(),name='submitbug'),
    path('author/',author.as_view(),name='author'),
    path('my_article/',my_article.as_view(),name='my_article'),
]
