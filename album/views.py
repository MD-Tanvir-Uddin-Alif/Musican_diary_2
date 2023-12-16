from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import addalbum
from .models import Album
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def add_album(request):
    if request.method == 'POST':
        album_form = addalbum(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('home_page')
    else:
        album_form = addalbum()
    return render(request,'album.html',{'form':album_form})


class AddAlbumClassView(CreateView):
    model = Album
    form_class = addalbum
    template_name = 'album.html'
    success_url = reverse_lazy('home_page')


def edit_album(request,id):
    album = Album.objects.get(pk=id)
    album_form = addalbum(instance=album)
    if request.method == 'POST':
        album_form = addalbum(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home_page')
        
    return render(request,'album.html',{'form':album_form})

class EditAlbumClassView(UpdateView):
    model = Album
    form_class = addalbum
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home_page')

def delete_album(request,id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('home_page')

class DeleteAlbumClassView(DeleteView):
    model =  Album
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home_page')
    template_name  = 'delete.html'