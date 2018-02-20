import re
import requests
from bs4 import BeautifulSoup


def get_artist_list(artist_name):

    url = 'https://www.melon.com/search/artist/index.htm'
    params = {
        'q': artist_name,
    }
    response = requests.get(url, params)
    source = response.text
    soup = BeautifulSoup(source, 'lxml')

    li_list = soup.select('div.section_atist div#pageList > div > ul > li')
    result = []
    for li in li_list:
        # 1) artist_id 추출
        artist_id = li.select_one('dd:nth-of-type(4) input').get('value')
        print(artist_id)

        # 2) name 추출
        artist_title = li.select_one('dt > a').get('title')
        name = re.search(r'(.*?)\s-', artist_title).group(1)
        print(name)

        url_img = li.select_one('div.wrap_atist12 > a > img').get('src')
        # 기본 프로필에서 이미지 주소가 html문서와 상이한 문제해결
        if url_img == 'http://cdnimg.melon.co.kr':
            url_img_cover = 'http://cdnimg.melon.co.kr/resource/image/web/default/noArtist_300_160727.jpg'
        else:
            url_img_cover = re.search(r'(.*.jpg)', url_img).group(1)
        print(url_img_cover)


        artist = Artist(
            artist_id=artist_id,
            name=name,
            url_img_cover=url_img_cover,
        )
        result.append(artist)
    return result




class Artist:
    def __init__(self, artist_id, name, url_img_cover):
        self.artist_id = artist_id
        self.name = name
        self.url_img_cover = url_img_cover

    def __str__(self):
        return f'{self.artist_id} {self.name} [{self.url_img_cover}]'


if __name__ == '__main__':
    result = get_artist_list('아이유')
    for i in result:
        print(i)