import traceback
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from django.views import View
import uuid, os
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from utils.send_email import send_register_email
from cs import settings


class index(View):
    def get(self,requests):
        return render(requests,'index/index.html')

class me(View):
    def get(self,requests):
        return render(requests,'index/me.html')
