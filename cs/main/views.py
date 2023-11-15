import traceback
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from django.views import View
import uuid, os
from django.contrib.auth.backends import ModelBackend

from utils.send_email import send_register_email
from cs import settings
from .models import Catgory, Post


class index(View):
    def get(self,requests):
        return render(requests,'index/index.html')

class me(View):
    def get(self,requests):
        return render(requests,'index/me.html')

class overall(View):
    def get(self,requests):
        catgorys = Catgory.objects.all()
        post_list = Post.objects.all()
        return render(requests,'article/overall.html',{'catgorys':catgorys,'post_list':post_list})
