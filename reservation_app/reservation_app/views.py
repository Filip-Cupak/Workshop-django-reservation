from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Room


def all_rooms_view(request:HttpRequest):
    all_rooms = Room.objects.all()
    return render(request, 'all_rooms.html', {'all_rooms': all_rooms})

def new_room_view(request:HttpRequest):
    if request.method == "POST":
        room_name = request.POST.get('room_name')
        room_capacity = request.POST.get('room_capacity')
        projector = request.POST.get('projector')

        if room_capacity < 0 and room_name is None:
            Error = "Wrong value"
            return render(request, 'new_room.html', {'Error': Error})

            return render(request,'all_rooms.html',{"room_name": room_name, "room_capacity": room_capacity, "projector": projector})


    return render(request, 'new_room.html')

def room_detail_view(request:HttpRequest):
    room = Room.objects.get(id=id)
    return render(request, 'room_detail.html', {'room': room})