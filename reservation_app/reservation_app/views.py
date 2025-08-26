from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest


def all_rooms_view(request:HttpRequest):
    return render(request, 'all_rooms.html')

def new_room_view(request:HttpRequest):
    if request.method == "POST":
        room_name = request.POST.get('room_name')
        room_capacity = request.POST.get('room_capacity')
        projector = request.POST.get('projector')
        return render(request,'all_rooms.html',{"room_name": room_name, "room_capacity": room_capacity, "projector": projector})


    return render(request, 'new_room.html')