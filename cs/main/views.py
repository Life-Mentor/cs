import traceback
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from django.views import View
from django.contrib.auth.backends import ModelBackend
from django.core.paginator import Paginator
import markdown

from utils.send_email import send_register_email
from cs import settings
from .models import Catgory, Post, SubmitBug as bug, User_Post
from .form import Submitbug

class index(View):
    def get(self,requests):
        return render(requests,'index/index.html')

class aboutus(View):
    def get(self,requests):
        return render(requests,'index/me.html')

class overall(View):
    def get(self,requests):
        catgorys = Catgory.objects.all()
        post_list = User_Post.objects.all()
        paginator = Paginator(post_list, 10)
        page_number = requests.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(requests,'article/overall.html',{'catgorys':catgorys,'post_list':post_list,"page_obj": page_obj})

class check(View):
    def get(self,requests,detailed_id):
        try:
            post_list = User_Post.objects.filter(id=detailed_id)
        except Exception as e:
            return HttpResponse('未查询到此文章')
        else:
            for post in post_list:
                post_ = markdown.markdown(post.content,extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                    'markdown.extensions.toc',
                    ])
            return render(requests,'article/detailed.html',{'post_list':post_})
        
class SubmitBug(View):
    def get(self,requests):
        form = Submitbug()
        return render(requests,'bug/SubmitBug.html',{'form':form})
    def post(self,requests):
        form = Submitbug(requests.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            Bug_name = form.cleaned_data['Bug_name']
            bug_desc = form.cleaned_data['Bug_desc']
            print(username,Bug_name,bug_desc)
            subug = bug()
            subug.Bug_name= Bug_name
            subug.submitname = username
            subug.Bug_desc = bug_desc
            subug.save()
        return render(requests,'bug/SubmitBug.html',{'form':form})
class author(View):
    def get(self,requests):
        return render(requests,'article/author.html')
    def post(self,requests):
        return render(requests,'article/author.html')
