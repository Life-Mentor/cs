import traceback
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from django.views import View
import uuid, os
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from .forms import Reirster, Login
from .models import EmailVerifyRecord, User_Info
from utils.send_email import send_register_email
from cs import settings

class MyBlack(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get((Q(username=username)|Q(email=username)))
            if user.check_password(password):
                return user;
        except Exception as e:
            return None
def gen_uuid():
    return str(uuid.uuid4())

class reirster(View):
    def get(self,request):
        form = Reirster()
        return render(request,'users/reirster.html',{'form':form})
    def post(self,request):
        code = '注册失败了，仔细检查一下'
        form = Reirster(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user_info = form.cleaned_data['user_info']
            img = form.cleaned_data['icon']

            file_name = gen_uuid() + img.name[img.name.rfind('.'):]
            file_path = os.path.join(settings.MEDIA_ROOT+"uploads/",file_name)
            print(file_path)
            with open(file_path,'wb') as fp:
                for part in img.chunks():
                    fp.write(part)
                    fp.flush()

            user = User_Info()
            user.name = username
            user.password =pwd
            user.email = email
            user.user_info = user_info
            user.icon = 'uploads/'+file_name
            user.save()
            send_register_email(form.cleaned_data.get('email'),'register')
            code = '注册成功'
            return render(request,'users/reirster.html',{'form':form,'code':code})
        return render(request,'users/reirster.html',{'form':form,'code':code})

class login(View):
    def get(self,request):
        form = Login()
        return render(request,'users/login.html',{'form':form})
    def post(self,request):
        code = '账号或者密码错误，仔细检查一下'
        form = Login(request.POST)
        if form.is_valid():
            username  = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User_Info.objects.filter(name=username,password=password)
            if user.exists():
                user = user.first()
                responses = redirect(reverse('main:index'))
                responses.set_cookie("userid",user.id)
                return responses
        return render(request,'users/login.html',{'form':form,'code':code})

def active_user(request,active_code):
    try:
        all_records = EmailVerifyRecord.objects.filter(code = active_code)
    except:
        return HttpResponse('404')
    if all_records.exists():
        for recod in all_records:
            email = recod.email
            user = User_Info.objects.get(email=email)
            user.is_staff = True
            user.save()
    else:
        return HttpResponse('请确认链接是否正确，以及注册是否成功')
    return redirect('secondary:login')

def home(request):
    userid = request.COOKIES.get('userid',0)
    if userid != 0:
        user = User_Info.objects.filter(id=userid).first()
        return render(request,'users/home.html',{'user':user})
    else:
        return HttpResponse('你可能没有登录')
