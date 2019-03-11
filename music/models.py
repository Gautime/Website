# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Album(models.Model): #/every model has to inherit from model.Model/
	artist = models.CharField(max_length= 250) #/Charfield tell the type of data artist column is holding/
	album_name = models.CharField(max_length= 500)
	genre = models.CharField(max_length=500)
	album_logo = models.FileField() #/to upload logofiles from the user/

	def get_absolute_url (self):
		return reverse('music:details', kwargs={'pk':self.pk}) #/kwargs is keyword args.......self.pk is for addition of created album to database/

	def __str__(self):
		return self.album_name + ' - ' + self.artist

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE) #/on delete models.Cascade allows you to delete song if the album is deleted./
	file_type = models.CharField(max_length=10)
	song_title= models.CharField(max_length=50)
	is_favourite = models.BooleanField(default= False)
	def __str__(self):
		return self.song_title


