from django.shortcuts import render
from django.views import View

class index(View):
    def get(self,requests):
        return render(requests,'index/index.html')

