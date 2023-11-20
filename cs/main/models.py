from django.db import models
from secondary import models as m
from mdeditor.fields import MDTextField

class Catgory(models.Model):
    name = models.CharField(max_length=32, verbose_name='分类名称')
    desc = models.TextField(max_length=255, blank=True, null=True,default='',verbose_name='分类描述')
    add_data = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    class Meat:
        verbose_name='博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name='文章标签')
    add_data = models.DateTimeField(auto_now=True,verbose_name='修改时间')
    pub_data = models.DateTimeField(auto_now=True, verbose_name='修改时间')

class Post(models.Model):
    """ 即将废弃 """
    title = models.CharField(max_length=61, verbose_name='文章标题')
    desc = models.TextField(max_length=200,verbose_name='文章内容',blank=True,default='')
    catgory = models.ForeignKey(Catgory,on_delete=models.CASCADE, verbose_name='文章标签')
    content = models.TextField(verbose_name='文章标题',blank=True,null=True)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='文章标签')
    owner = models.ForeignKey(m.User_Info, on_delete=models.CASCADE,verbose_name='作者')
    add_data = models.DateTimeField(verbose_name='添加时间')
    pub_data = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meat:
        verbose_name='博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class SubmitBug(models.Model):
    submitname= models.CharField(max_length=32,verbose_name='用户名字',default='匿名用户')
    Bug_name = models.CharField(max_length=56,verbose_name='bug名字')
    Bug_desc = models.CharField(max_length=256,verbose_name='bug描述')

class User_Post(models.Model):
    title = models.CharField(max_length=32,verbose_name='文章标题')
    content = MDTextField(verbose_name='具体内容')
    owner = models.ForeignKey(m.User_Info, on_delete=models.CASCADE,verbose_name='作者')
    catgory = models.ForeignKey(Catgory,on_delete=models.CASCADE, verbose_name='文章分类')
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='文章标签')
    class Meat:
        verbose_name='用户文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
