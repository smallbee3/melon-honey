from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from artist.models import Artist


def artist_list(request):

    artists = Artist.objects.all()
    context = {
        'artists': artists,

    }
    return render(
        request,
        'artist/artist_list.html',
        context,
    )


def artist_add(request):


    if request.method == 'POST':

        # return HttpResponse(name)


        name = request.POST['name']
        birthday_text = request.POST['birthday']
        birth_date = datetime.strptime(birthday_text, '%Y.%m.%d')

        intro = request.POST['intro']



        Artist.objects.create(
            name=name,
            birth_date=birth_date,
            intro=intro,
        )

        return redirect('artist:artist-list')
    else:
        return render(request, 'artist/artist_add.html')
    #     return HttpResponse('바보')

