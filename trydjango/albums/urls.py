from django.urls import path
from .views import (
    album_create_view,
    album_list_view,
    album_delete_view
)

app_name = 'albums'
urlpatterns = [
    path('create/', album_create_view, name='album_create'),
    path('', album_list_view, name='album_list'),
    path(r'<int:id>/', album_delete_view, name='album_delete'),
]