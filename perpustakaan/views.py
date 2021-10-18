from django.shortcuts import render
from perpustakaan.models import Buku
from perpustakaan.form import FormBuku

# Create your views here.
# ORM
# import dulu database Buku (from perpustakaan.models import Buku)

# FORM
# dibuat setelah membuat form.py ()

# digunakan sebelum membuat database, tujuanya untuk mengecek
# def buku(request):
#     judul = ["Belajar Django", "Belajar Python", "Belajar Bootstrap"]
#     penulis = "ricko yogga"
#     konteks = {
#         'judul': judul,
#         'penulis': penulis
#     }
#     return render(request, 'buku.html', konteks)

# ketika sudah membuat database gunakan ini (ORM) lalu ubah syntax di buku.html
def buku(request):
    books = Buku.objects.all()

    konteks = {
        'books': books,
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return render(request, 'penerbit.html')


# FORM
# dibuat setelah membuat form.py 
# ini dibuat sebelum membuat CRUD

# def tambah_buku(request):
#     form = FormBuku()

#     konteks = {
#         'form': form,
#     }

#     return render(request, 'tambah-buku.html', konteks)


# CRUD
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = "Data berhasil disimpan"

        konteks = {
            'form': form,
            'pesan' : pesan,
        }
        return render(request, 'tambah-buku.html', konteks)

    else:
        form = FormBuku()

        konteks = {
            'form' : form,
        }
    return render(request, 'tambah-buku.html', konteks)