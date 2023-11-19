# CkEditor

关闭标签过滤safe

```
{{ bl|safe}}
```



```shell
pip install django-ckeditor
pip install pillow
```

setting.py

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = os.path.join(BASE_DIR, "static",'ckeditor')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # 默认根目录
CKEDITOR_UPLOAD_PATH=os.path.join(BASE_DIR,'media','uploads')
CKEDITOR_IMAGE_BACKEND = 'pillow'

INSTALLED_APPS = [
    'edit',
    'ckeditor',
]

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Save', 'Preview', '-', 'Templates','Find', 'Replace']},

            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', '-',
                       'JustifyLeft', 'JustifyCenter', '-']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar']},

            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},

            {'name': 'yourcustomtools', 'items': [
                'Preview',
                'Maximize',
            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}


```

urls.py

```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('edit.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



models.py

```python
from django.db import models
# 不带图片上传
from ckeditor.fields import RichTextField
# 带图片上传
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class MyNote(models.Model):
    title = models.CharField(max_length=64, default='a default title')
    content = RichTextUploadingField(config_name='default')
```



admin.py

```python
from django.contrib import admin
from .models import MyNote
# Register your models here.
admin.site.register(MyNote)
```

forms.py

```python
from django import forms
from .models import MyNote

class NoteForm(forms.ModelForm):
    class Meta:
        model = MyNote
        fields = ['title', 'content']
```



views.py

```python
from django.shortcuts import render
from .forms import NoteForm
# Create your views here.

def index(request):
    return render(request,'index.html', {'form': NoteForm()})
```

index.html

```html
<script src="/static/ckeditor/ckeditor/ckeditor-init.js"></script>
<script src="/static/ckeditor/ckeditor/ckeditor/ckeditor.js"></script>

{% block content %}
<div class="left">
    <form method="post" action="/">
        {% csrf_token %}
        {{form.as_p}}
    </form>
</div>
{% endblock %}
```

app urls.py

```python
from django.urls import path, include
from edit import views
urlpatterns = [
    path('',views.index),
]

```



复制ckeditor文件

```shell
python manage.py collectstatic
```

数据库迁移

```shell
python manage.py  makemigrations
python manage.py migrate
```



运行

```shell
python manage.py runserver
```

