import re
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime

from ...models import Artist


def artist_add_from_melon(request):

    print(request.POST)
    artist_id = request.POST.get('artist_id')

    if artist_id:
        import requests
        from bs4 import BeautifulSoup

        url = f'https://www.melon.com/artist/detail.htm'
        params = {
            'artistId': artist_id,
        }
        response = requests.get(url, params)
        source = response.text
        soup = BeautifulSoup(source, 'lxml')

        # name
        name = soup.select_one('p.title_atist').strong.next_sibling

        # url_img_cover
        url_image = soup.select_one('span#artistImgArea > img').get('src')
        # url_img_cover = re.search(r'', url_image)

        personal_information = {}
        if re.search(r'신상정보</h3>', source, re.DOTALL):
            dl_list = re.search(r'신상정보</h3>.*?-->(.*?)</dl>', source, re.DOTALL)
            # dt = re.findall('<dt>.*?</dt>', dl_list.group(1))
            # dd = re.findall('<dd>.*?</dd>', dl_list.group(1))
            soup = BeautifulSoup(dl_list.group(), 'lxml')
            dt = soup.select('dt')
            dd = soup.select('dd')

            dd_dt = list(zip(dt, dd))
            # print(dd_dt)

            for i, j in dd_dt:
                i = i.get_text(strip=True)
                j = j.get_text(strip=True)
                personal_information[i] = j
            # print(self._personal_information)
        else:
            personal_information = ''

        # url_img_cover = artist.url_img_cover
        real_name = personal_information.get('본명')
        nationality = personal_information.get('국적')
        constellation = personal_information.get('별자리')
        birth_date = personal_information.get('생일')

        # response = requests.get(url_img_cover)
        # binary_data = response.content
        # temp_file = BytesIO(


        Artist.objects.create(
            artist_id=artist_id,
            name=name,
            real_name=real_name,
            nationality=nationality,
            birth_date=datetime.strptime(birth_date, '%Y.%m.%d'),
            constellation=constellation,
            # blood_type='',
        )

    return redirect('artist:artist-list')

    # return HttpResponse(url_img_cover)





    '''
    artist_id
    name
    real_name
    nationality
    birth_date
    constellation
    blood_type
    intro
    '''