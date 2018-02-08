from datetime import datetime
from django.utils import timezone


from django.db import models

from album.models import Album
from artist.models import Artist

# Artist
#   - Album
#       - Song
#       - Song
#       - Song


class Song(models.Model):
    title = models.CharField('곡 제목', max_length=255)
    artist = models.ManyToManyField(
        Artist,
        # through='ArtistSong',
        verbose_name='가수',
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        verbose_name='앨범',
        # blank=True,
        null=True,
    )     # through_fields=('artist', 'song')) # (상위개념, 하위개념)
          # -> 한노래에 가수 여러명, 가수가 노래 여러개
    # 보통 중간자모델이 아래에 있어서 ''string으로 해주는 것.
    # 수업시간

    release_date = models.DateField('발매일', blank=True, null=True)
    genre = models.CharField('장르', max_length=100, blank=True)

    # flac = models.CharField('FLAC', max_length=100, blank=True)
    lyrics = models.TextField('가사', max_length=10000, blank=True)

    # writing = models.CharField('작사', max_length=30, blank=True)
    # composing = models.CharField('작곡', max_length=30, blank=True)
    # arranging = models.CharField('편곡', max_length=30, blank=True)

    @property
    def artist(self):
        return self.album.artists.all()

    @property
    def release_date(self):
        return self.album.release_date

    @property
    def formatted_release_date(self):
        # 2017.01.15

        # return self.album.release_date

        return self.album.release_date.strftime('%Y.%m.%d')

    # datetime.strftime(
    #     # timezone.make_naive(self.created_date),
    #     timezone.localtime(self.created_date),
    #     '%Y.%m.%d'),



    def __str__(self):
        artists = ', '.join(self.album.artists.values_list('name', flat=True))
        return f'{artists} - {self.title} ({self.album.title})'
        # return self.title




class ArtistSong(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    demo_date = models.DateTimeField(null=True) # -> 초기 데이터 없어서 에러남.
    # producer = models.ForeignKey() -> through_field해야되서 일단 뺌.

    def __str__(self):
        return f'{self.artist} - {self.song}'