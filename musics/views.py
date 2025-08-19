from django.shortcuts import render, redirect

from musics.forms import AlbumCreateForm, AlbumEditForm, SongCreateForm
from musics.models import Album, Song

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Create your views here.


def index_view(request):

    albums = Album.objects.all()
    context = {'albums': albums}

    return render(request, 'common/index.html', context)



def create_album_view(request):

    if request.method == "GET":
        form = AlbumCreateForm
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}

    return render(request, 'albums/create-album.html', context)

def edit_album_view(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == "GET":
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            album.save()
            return redirect('index')
    context = {'form': form, 'album': album}

    return render(request, 'albums/edit-album.html', context)

def delete_album_view(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == "GET":
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            album.delete()
            return redirect('index')
    context = {'form': form, 'album': album}

    return render(request, 'albums/delete-album.html', context)

def album_details_view(request, pk):
    album = Album.objects.get(id=pk)
    songs = album.songs.all()
    context = {'album': album, 'songs': songs}

    return render(request, 'albums/album-details.html', context)


def create_song_view(request):
    if request.method == "POST":
        form = SongCreateForm(request.POST, request.FILES)
        if form.is_valid():

            song = form.save(commit=False)


            uploaded_file = request.FILES['music_file_data']
            song.music_file_data = uploaded_file.read()


            song.save()

            return redirect('index')
    else:
        form = SongCreateForm()

    context = {'form': form}
    return render(request, 'songs/create-song.html', context)


def play_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    album = song.album

    context = {'song': song, 'album': album}
    return render(request, 'songs/music-player.html', context)

def serve_song(request, album_id, song_id):
    song = get_object_or_404(Song, id=song_id, album_id=album_id)

    response = HttpResponse(song.music_file_data, content_type='audio/mpeg')
    response['Content-Disposition'] = f'inline; filename="{song.song_name}.mp3"'

    return response


