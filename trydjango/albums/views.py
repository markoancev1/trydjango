from django.shortcuts import render, redirect, reverse

from .models import Album

from .forms import AlbumForm

from django.http import HttpResponseRedirect

# Create your views here.


def album_create_view(request):
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AlbumForm()
    context = {
        'form': form
    }
    return render(request, "albums/album_create.html", context)


def album_list_view(request):
    queryset = Album.objects.all().order_by('album_name')
    context = {
        "object_list": queryset
    }
    return render(request, "albums/album_list.html", context)


def album_delete_view(request, id):
    obj = Album.objects.filter(id=id)
    obj.delete()
    return redirect('/albums/')
