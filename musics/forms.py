from django import forms

from musics.models import Album, Song


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class AlbumCreateForm(AlbumBaseForm):
    pass

class AlbumEditForm(AlbumBaseForm):
    pass

class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields.values():
            fields.widget.attrs['ReadOnly'] = True

class SongBaseForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'


class SongCreateForm(SongBaseForm):
    music_file_data = forms.FileField(
        label="Music File: ",
        required=True,
    )
