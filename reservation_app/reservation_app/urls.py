from django.urls import path
from .views import new_room_view, all_rooms_view, room_detail_view

urlpatterns = [

    path('add/', new_room_view, name='new_room'),
    path('', all_rooms_view, name='all_rooms'),
    path('room_detail/<int:id>', room_detail_view, name='room_detail'),
    ]