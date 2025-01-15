from django.db import models

# Create your models here.
class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    video = models.FileField(upload_to='videos/')
    posters = models.ImageField(upload_to='posters/')


class Actors(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Genres(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Videos_Actors(models.Model):
    id = models.IntegerField(primary_key=True)
    video_id = models.ForeignKey(Video)
    actors_id = models.ForeignKey(Actors)


class Videos_Genres(models.Model):
    id = models.IntegerField(primary_key=True)
    videos_id = models.ForeignKey(Video)
    genres_id = models.ForeignKey(Genres)