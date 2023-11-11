from django.shortcuts import render
from django.views import View
import uuid, os
from .forms import Reirster
from .models import UserInfo
from cs import settings

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
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.email = form.cleaned_data.get('email')
            user_info = form.cleaned_data.get('user_info')
            img = form.cleaned_data['icon']
            new_user.save()
            file_name = gen_uuid() + img.name[img.name.rfind('.'):]
            file_path = os.path.join(settings.MEDIA_ROOT+'uploads/',file_name)
            print(file_path)
            with open(file_path,'wb') as fp:
                for part in img.chunks():
                    fp.write(part)
                    fp.flush()
            user = UserInfo()
            user.user_info = user_info
            user.icon = 'uploads/'+file_name
            code = '注册成功'
            return render(request,'users/reirster.html',{'form':form,'code':code})
        return render(request,'users/reirster.html',{'form':form,'code':code})


