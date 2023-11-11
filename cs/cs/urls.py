from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(("main.urls","main"),namespace="main")),
    path('users/',include(("secondary.urls","secondary"),namespace="secondary")),
]
