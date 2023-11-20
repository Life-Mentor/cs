from django.shortcuts import render, HttpResponse
from django.views import View
from django.core.paginator import Paginator
import markdown

from cs import settings
from .models import Catgory, SubmitBug as bug, Tag, User_Post
from .form import Submitbug, User_post
from secondary.models import User_Info

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
                    'markdown.extensions.tables'
                    ])
                author = post.owner.name
            return render(requests,'article/detailed.html',{'post_list':post_,'author':author})
        
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
            subug = bug()
            subug.Bug_name= Bug_name
            subug.submitname = username
            subug.Bug_desc = bug_desc
            subug.save()
        return render(requests,'bug/SubmitBug.html',{'form':form})
class author(View):
    def get(self,requests):
        user_post =  User_Post.objects.all()
        form = User_post()
        return render(requests,'article/author.html',{'forms':form})
    def post(self,requests):
        form = User_post(requests.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            title = form.cleaned_data.get('title')
            author_user = form.cleaned_data.get('username')
            userpost = User_Post()
            c = form.cleaned_data.get('catgory')
            catgory = Catgory.objects.get(name = c)
            if c is None:
                c = "随笔杂记"
            tags = form.cleaned_data.get('tags')
            if tags is None:
                tags = "随笔杂记"

            try:
                post_list = User_Info.objects.filter(name=author_user)
            except Exception as e:
                return HttpResponse("你可能还没有注册")
            else:
                if post_list.exists():
                    user = User_Info.objects.get(name = author_user)
                    tag = Tag.objects.get(name = tags)
                    userpost.content = content
                    userpost.title = title
                    userpost.owner = user
                    userpost.catgory = catgory
                    userpost.tags = tag
                    userpost.save()

            return render(requests,'article/author.html',{"forms":form})
        return render(requests,'article/author.html',{"forms":form})

