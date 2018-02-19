from django.http import HttpResponse
from django.shortcuts import render

from song.models import Song


def song_list(request):

    songs = Song.objects.all()
    context = {
        'songs': songs,

    }
    return render(
        request,
        'song/song_list.html',
        context,
    )


def song_search(request):

    context = {}

    if request.method == 'POST':

        keyword = request.POST['keyword'].strip()

        if keyword:
            # return HttpResponse(keyword)

            songs = Song.objects.filter(title__contains=keyword)
            # context = {
            #     'songs': songs,
            # }
            context['songs'] = songs
    #     return render(request, 'song/song_search.html', context)
    # else:
    #     return render(request, 'song/song_search.html')
    return render(request, 'song/song_search.html', context)
