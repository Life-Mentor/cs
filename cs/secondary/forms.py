from django import forms
from django.contrib.auth.models import User
from PIL import Image
from django.forms import widgets
from .models import User_Info

class Reirster(forms.ModelForm):
    username = forms.CharField(label='用户名',max_length=25,widget=forms.TextInput(attrs={'class':'input is-success','placeholder':'用户名','style':"width:180px;"}))
    email = forms.EmailField(label='邮箱', max_length=32, widget=forms.EmailInput(attrs={ 'class': 'input is-success', 'placeholder': '邮箱','style':"width:220px;"}))
    password = forms.CharField(label='密码',max_length=8,widget=forms.PasswordInput(attrs={'class':'input is-success',"placeholder":"密码",'style':"width:220px;"}))
    icon = forms.ImageField(label='用户头像',widget=forms.FileInput(attrs = {'class':''}))
    # user_info = forms.CharField(label='个人简介',max_length=256,widget=forms.TextInput(attrs={'class':'textarea is-success','placeholder':'个人简介.... ','style':"width=400"}))
    user_info = forms.CharField(widget=forms.Textarea(attrs={'class':'','cols': '60', 'rows':'6','style':"width:220px;",'placeholder':'个人简介:'}))

    class Meta:
        model = User_Info
        fields = ('username','email','password','icon','user_info')

    def clean_email(self):
        """ 验证用户是否存在 """
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('此邮箱已被注册!')
        return email
    def clean_user(self):
        username = self.cleaned_data.get('username')
        exists = User.objects.filter(username=username).exists()
        if exists:
            raise forms.ValidationError('用户名已存在')
        return username

class Login(forms.Form):
    username = forms.CharField(label='用户名',max_length=25,widget=forms.TextInput(attrs={'class':'input is-success','placeholder':'用户名','style':"width:220px;"}))
    password = forms.CharField(label='密码',max_length=8,widget=forms.PasswordInput(attrs={'class':'input is-success',"placeholder":"密码",'style':"width:220px;"}))

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username == password:
            raise forms.ValidationError('用户名与密码不能相同')
        return password
