from django.urls import path

from artist.views import artist_list

app_name = 'artist'
urlpatterns = [
    path('', artist_list),
]