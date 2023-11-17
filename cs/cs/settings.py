import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-8*7b#!x6533_$!dz0ny4^x7t1b3#ou4egymu+&6^tfe&2qwyrc'
DEBUG = True
ALLOWED_HOSTS = ["*"]
AUTHENTICATION_BACKENDS = (
    'secondary.views.MyBlack',
)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main.apps.MainConfig',
    'secondary.apps.SecondaryConfig',
    'ckeditor',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'cs.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.media',  # 新加入的
            ],
        },
    },
]
WSGI_APPLICATION = 'cs.wsgi.application'

# DATABASES = { 'default': { 'ENGINE': 'django.db.backends.mysql', 'NAME': 'cs', 'USER': 'root', 'PASSWORD': 'qpal', 'HOST': '127.0.0.1', 'PORT': 3306, } }
DATABASES = { 'default': { 'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3', } }
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,"static")
# STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static"),]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'   # 用于发送电子邮件的主机。
EMAIL_HOST_USER = "959735909@qq.com"    # 自己的邮箱地址
EMAIL_HOST_PASSWORD = "ryrekrdqvxezbege"       # 自己的邮箱密码
EMAIL_PORT = 25
EMAIL_USE_SSL = True
