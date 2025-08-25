from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest


def all_rooms(request:HttpRequest):
    return render(request, 'all_rooms.html')

def new_room(request:HttpRequest):
    return render(request, 'new_room.html')