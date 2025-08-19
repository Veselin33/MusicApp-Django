from django.urls import path, include

from musics.views import index_view, create_album_view, edit_album_view, delete_album_view, album_details_view, \
    create_song_view, serve_song, play_song

urlpatterns = [

    path('', index_view, name='index'),
    path('album/', include([
        path('create/', create_album_view, name='create-album'),
        path('edit/<int:pk>/', edit_album_view, name='edit-album'),
        path('delete/<int:pk>/', delete_album_view, name='delete-album'),
        path('details/<int:pk>/', album_details_view, name='details-album')
    ])),
    path('song/', include([
        path('create/', create_song_view, name='create-song'),
        path('serve-song/<int:album_id>/<int:song_id>/', serve_song, name='serve-song'),
        path('play-song/<int:pk>/', play_song, name='play-song'),
    ]))

]