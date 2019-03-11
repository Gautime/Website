from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
	# /music/
    url(r'^$', views.IndexView.as_view(), name='index'), 
    
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/music/album_id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name = 'details'),
    #music/album/add/ --- pk hasnt been specified cause it is  a new album and hasnt been given a pk yet
	url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

	url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

	url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),


 

 ]