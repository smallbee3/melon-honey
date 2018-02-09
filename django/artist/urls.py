from django.urls import path

from artist.views import artist_list, artist_add

app_name = 'artist'
urlpatterns = [
    path('', artist_list, name='artist-list'),
    path('add/', artist_add, name='artist-add'),
]