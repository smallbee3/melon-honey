from django.urls import path

from song.views import song_list

app_name = 'song'
urlpatterns = [
    path('', song_list),
]