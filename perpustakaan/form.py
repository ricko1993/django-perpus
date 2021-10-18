# membuat form
# selengkapnya di https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/#modelform
from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku


class FormBuku(ModelForm):
    class Meta:
        model = Buku
        # untuk menampilkan semua data didatabase Buku
        fields = '__all__'

        # untuk menampilkan beberapa field yang ada didalam database Buku
        # fields = ['judul', 'penulis', 'kelompok_id']

        # untuk mengecualikan field yang tampil gunakan exclude
        # exclude = ['penerbit']

        # menambahkan widget
        # jangan lupa import form "from django import forms"
        # input widget sesuai tipe
        widgets = {
            'judul' : forms.TextInput({'class':'form-control'}),
            'penulis' : forms.TextInput({'class':'form-control'}),
            'penerbit' : forms.TextInput({'class':'form-control'}),
            'jumlah' : forms.NumberInput({'class':'form-control'}),
            'kelompok_id' : forms.Select({'class':'form-control'}),
        }