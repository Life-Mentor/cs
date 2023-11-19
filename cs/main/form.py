from ckeditor_uploader.fields import fields
from django import forms
from .models import SubmitBug, test as t

class Submitbug(forms.ModelForm):
    username = forms.CharField(label='用户名',max_length=25,widget=forms.TextInput(attrs={'class':'input is-success','placeholder':'用户名','style':"width:220px;"}))
    Bug_name = forms.CharField(label='bug的名字',max_length=25,widget=forms.TextInput(attrs={'class':'input is-success','placeholder':'bug的名字','style':"width:220px;"}))
    Bug_desc = forms.CharField(label='bug的描述',widget=forms.Textarea(attrs={'class':'','cols': '60', 'rows':'6','style':"width:220px;",'placeholder':'对bug进行一个简单描述:网址，报错信息都可以'}))

    class Meta:
        model = SubmitBug
        fields = ('submitname','Bug_name','Bug_desc')

class test(forms.ModelForm):
    class Meta:
        model = t
        fields = ['content']

