from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator
import markdown

from .models import Catgory, SubmitBug as bug, Tag, User_Post, suggestion as su, Discuss
from .form import Submitbug, User_post, suggestion as SU, discuss
from secondary.models import User_Info

def logout(requests):
    responses = redirect(reverse('main:index'))
    responses.delete_cookie('userid')
    return responses

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
        form = discuss()
        users = requests.COOKIES.get("userid")
        if users != 0 and users is not None:
            user = User_Info.objects.get(id=users)
        else:
            return HttpResponse("请先登录")

        try:
            post_list = User_Post.objects.filter(id=detailed_id)
        except Exception as e:
            return HttpResponse('未查询到此文章')
        else:
            # ------------------
            try:
                post_user = User_Post.objects.get(id=detailed_id)
            except:
                return HttpResponse("获取失败，是不是想干我网站")
            discus = Discuss.objects.filter(belong=post_user)
            #-------------------
            for post in post_list:
                post_ = markdown.markdown(post.content,extensions=[ 'markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc', 'markdown.extensions.tables' ])
                author = post.owner.name
                title = post.title
                return render(requests,'article/detailed.html',{'post_list':post_,'author':author,"title":title,"form":form,"userinfo":user,"discus":discus})
    def post(self,requests,detailed_id):
        form = discuss(requests.POST)
        if form.is_valid():
            users = requests.COOKIES.get("userid")
            if users != 0 and users is not None:
                user = User_Info.objects.get(id=users)
            else:
                return HttpResponse("请先登录")
            desc = form.cleaned_data.get('desc')
            discus = Discuss()
            discus.name = user
            discus.desc = desc
            post_user = User_Post.objects.get(id=detailed_id)
            discus.belong = post_user
            discus.save()
        try:
            post_list = User_Post.objects.filter(id=detailed_id)
        except Exception as e:
            return HttpResponse('未查询到此文章')
        else:
            # ------------------
            try:
                post_user = User_Post.objects.get(id=detailed_id)
            except:
                return HttpResponse("获取失败，是不是想干我网站")
            discus = Discuss.objects.filter(belong=post_user)

            #-------------------
            for post in post_list:
                post_ = markdown.markdown(post.content,extensions=[ 'markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc', 'markdown.extensions.tables' ])
                author = post.owner.name
                title = post.title
                users = requests.COOKIES.get("userid")
                if users != 0:
                    user = User_Info.objects.get(id=users)
                else:
                    return HttpResponse("请先登录")
                return render(requests,'article/detailed.html',{'post_list':post_,'author':author,"title":title,"form":form,"userinfo":user,"discus":discus})
        return render(requests,'article/detailed.html')
        
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
        form = User_post()
        return render(requests,'article/author.html',{'forms':form})
    def post(self,requests):
        form = User_post(requests.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            title = form.cleaned_data.get('title')
            author_user = requests.COOKIES.get('userid')
            userpost = User_Post()
            c = form.cleaned_data.get('catgory')
            catgory = Catgory.objects.get(name = c)
            if c is None:
                c = "随笔杂记"
            tags = form.cleaned_data.get('tags')
            if tags is None:
                tags = "随笔杂记"

            try:
                post_list = User_Info.objects.filter(id=author_user)
            except Exception as e:
                return HttpResponse("你可能还没有注册")
            else:
                if post_list.exists():
                    user = User_Info.objects.get(id = author_user)
                    tag = Tag.objects.get(name = tags)
                    userpost.content = content
                    userpost.title = title
                    userpost.owner = user
                    userpost.catgory = catgory
                    userpost.tags = tag
                    userpost.save()
            return render(requests,'article/author.html',{"forms":form,"code":"发布成功"})
        return render(requests,'article/author.html',{"forms":form})
class my_article(View):
    def get(self,requests):
        userid = requests.COOKIES.get('userid')
        users = User_Info.objects.get(id = userid)
        if users:
            post_list = User_Post.objects.filter(owner = users.id)
            return render(requests,'article/my_article.html',{"post_list":post_list,"users":users})
        return render(requests,'article/my_article.html')
    def post(self,requests):
        return render(requests,'article/my_article.html')

class suggestion(View):
    def get(self,requests):
        form = SU()
        return render(requests,'suggestion/index.html',{"form":form})
    def post(self,requests):
        form = SU(requests.POST)
        if form.is_valid():
            su_name = form.cleaned_data.get('su_name')
            su_title = form.cleaned_data.get('su_title')
            su_desc = form.cleaned_data.get('su_desc')
            sus = su()
            sus.su_name = su_name
            sus.su_title = su_title
            sus.su_desc = su_desc
            sus.save()
        return render(requests,'suggestion/index.html',{"form":form,"code":"反馈成功，我们会讨论您所提的建议"})
def not_404(requests,exception=None):
    return render(requests,"errors/404.html")

def not_403(requests,exception=None):
    return render(requests,"errors/403.html")

