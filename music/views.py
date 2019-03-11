# -*- coding: utf-8 -*-
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .models import Album
from .forms import UserForms

class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums' #/dictionary to get content your tempelate needs/

	def get_queryset(self): #/querying database for all albums/
		return Album.objects.all()

class DetailsView(generic.DetailView):
	model = Album
	template_name = 'music/details.html'

class AlbumCreate(CreateView):
  	model = Album
	fields =['artist', 'album_name', 'genre', 'album_logo'] #/List of fields you want user to add while creating, may contain all or some/ 

class AlbumUpdate(UpdateView):
	model = Album
	fields =['artist', 'album_name', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
	model = Album
	success_url=reverse_lazy('music:index')

class UserFormView(View):
	form_class = UserForms
	template_name = 'music/registration_form.html'

	#display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	#process form data after user submits
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit = False)

			#clean normalized data
			username =form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns user objects if credentials are correct

			user = authenticate(username=username, password= password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('music:index')

		# if the user didnt login or the account is blocked, we return the blank form again
		return render(request, self.template_name, {'form':form})






