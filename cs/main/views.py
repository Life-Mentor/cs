import traceback
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from django.views import View
from django.contrib.auth.backends import ModelBackend

from utils.send_email import send_register_email
from cs import settings
from .models import Catgory, Post


class index(View):
    def get(self,requests):
        return render(requests,'index/index.html')

class aboutus(View):
    def get(self,requests):
        return render(requests,'index/me.html')

class overall(View):
    def get(self,requests):
        catgorys = Catgory.objects.all()
        post_list = Post.objects.all()
        return render(requests,'article/overall.html',{'catgorys':catgorys,'post_list':post_list})

class check(View):
    def get(self,requests,detailed_id):
        try:
            post_list = Post.objects.filter(id=detailed_id)
        except Exception as e:
            return HttpResponse('未查询到此文章')
        else:
            return render(requests,'article/detailed.html',{'post_list':post_list})
        
