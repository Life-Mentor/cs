from django.shortcuts import render
from django.views import View

def index(requests):
    return render(requests,"chat/index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
