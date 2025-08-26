from django.urls import path
from .views import new_room, all_rooms

urlpatterns = [

    path('add/', new_room, name='new_room'),
    path('', all_rooms, name='all_rooms'),
    ]