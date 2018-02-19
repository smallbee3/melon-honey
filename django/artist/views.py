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
        real_name = request.POST['real_name']
        nationality = request.POST['nationality']
        constellation = request.POST['constellation']
        blood_type = request.POST['blood_type']

        intro = request.POST['intro']

        if request.POST['birth_date']:
            birthday_text = request.POST['birth_date']
            birth_date = datetime.strptime(birthday_text, '%Y-%m-%d')
        else:
            birth_date = None

        Artist.objects.create(
            name=name,
            real_name=real_name,
            nationality=nationality,
            birth_date=birth_date,
            constellation=constellation,
            blood_type=blood_type,
            intro=intro,
        )

        return redirect('artist:artist-list')
    else:
        return render(request, 'artist/artist_add.html')
    #     return HttpResponse('바보')

