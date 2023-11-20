from django import forms
from .models import SubmitBug, User_Post
from mdeditor.fields import MDTextField

class Submitbug(forms.ModelForm):
    username = forms.CharField(label='用户名',max_length=25,widget=forms.TextInput(attrs={'class':'input is-success','placeholder':'用户名','style':"width:220px;"}))
    Bug_name = forms.CharField(label='bug的名字',max_length=25,widget=forms.TextInput(attrs={'class':'input is-success','placeholder':'bug的名字','style':"width:220px;"}))
    Bug_desc = forms.CharField(label='bug的描述',widget=forms.Textarea(attrs={'class':'','cols': '60', 'rows':'6','style':"width:220px;",'placeholder':'对bug进行一个简单描述:网址，报错信息都可以'}))

    class Meta:
        model = SubmitBug
        fields = ('submitname','Bug_name','Bug_desc')

class User_post(forms.ModelForm):
    title = forms.CharField(label='文章标题',max_length=25,widget=forms.TextInput(attrs={'class':'input is-success','placeholder':'文章标题','style':"width:220px;"}))
    content = MDTextField()
    username = forms.CharField(label='作者名称',max_length=25,widget=forms.TextInput(attrs={'class':'input is-success','placeholder':'作者名','style':"width:220px;"}))
    catgory = forms.CharField(label='文章分类',max_length=25,widget=forms.TextInput(attrs={'class':'input is-success','placeholder':'不知道写什么就"随笔杂记"','style':"width:220px;"}))
    tags = forms.CharField(label='文章标签',max_length=25,widget=forms.TextInput(attrs={'class':'input is-success','placeholder':'不知道写什么就"随笔杂记"','style':"width:220px;"}))
    class Meta:
        model = User_Post
        fields = ['content']
