from django.db import models

class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
        unique=True,
    )
    image_url = models.URLField(
        max_length=200,
    )
    price = models.FloatField()


    def __str__(self):
        return self.album_name


class Song(models.Model):
    song_name = models.CharField(
        max_length=200,
    )
    album = models.ForeignKey(
        Album,
        related_name="songs",
        on_delete=models.CASCADE,
    )
    music_file_data = models.BinaryField()

    def __str__(self):
        return self.song_name
