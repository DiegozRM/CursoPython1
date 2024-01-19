from django.urls import path
from .views import functionRooms
from .views import functionUsers
from .views import functionReservation


rooms_url = [
    path('create_room', functionRooms.create_room, name='create_room'),
    path('get_room', functionRooms.get_room, name='get_room'),
    path('update_room', functionRooms.update_room, name='update_room'),
    path('delete_room', functionRooms.delete_room, name='delete_room'),
]

users_url = [
    path('create_user', functionUsers.create_user, name='create_user'),
    path('get_user', functionUsers.get_user, name='get_user'),
    path('get_user_id', functionUsers.get_user_id, name='get_user_id'),
    path('update_user', functionUsers.update_user, name='update_user'),
    path('delete_user', functionUsers.delete_user, name='delete_user'),
]

reservation_url = [
    path('create_reservation', functionReservation.create_reservation, name='create_reservation'),
    path('get_reservation', functionReservation.get_reservation, name='get_reservation'),
    path('update_reservation', functionReservation.update_reservation, name='update_reservation'),
    path('delete_reservation', functionReservation.delete_reservation, name='delete_reservation'),
]

urlpatterns = rooms_url + users_url + reservation_url  # Corregir la escritura de 'urlpatterns'
