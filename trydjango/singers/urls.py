from django.urls import path
from .views import (
    singer_create_view,
    singer_list_view,
    singer_delete_view,
    singer_update_view
)

app_name = 'singers'
urlpatterns = [
    path('create/', singer_create_view, name='singer_create'),
    path('', singer_list_view, name='singer_list'),
    path(r'<int:id>/', singer_delete_view, name='singer_delete'),
    path(r'<int:id>/update/', singer_update_view, name='update'),

]
