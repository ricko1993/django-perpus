from django.shortcuts import render, redirect, HttpResponse
from perpustakaan.models import Buku
from perpustakaan.form import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from perpustakaan.resource import BukuResource

def export_xls(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachmen; filename="laporan buku.xls"'
    return response

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


# membuat form signup (daftar)
@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil dibuat!")
            return redirect('signup')
        else :
            messages.error(request, "Terjadi kesalahan!")
            return redirect('signup')
    else :
        form = UserCreationForm()
        konteks = {
            'form':form,
        }
    return render(request, 'signup.html', konteks)


# CRUD "DELETE"
@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    return redirect('buku')

# CRUD "UPDATE"
# dibuat setelah membuat CREATE

# ini salah g tau kenapa
# def ubah_buku(request, id_buku):
#     buku = Buku.objects.get(id=id_buku)
#     template = 'ubah-buku.html'
#     if request.POST:
#         form = FormBuku(request.POST, instance=buku)
#         if form.is_valid():
#             form.save()
#             return redirect('ubah_buku', id_buku=id_buku)
#         else:
#             form = FormBuku(instance=buku)
#             konteks ={
#                 'form':form,
#                 'buku':buku,
#             }
#         return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui!")
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form':form,
            'buku':buku,
        }
    return render(request, template, konteks)



# ketika sudah membuat database gunakan ini (ORM) lalu ubah syntax di buku.html
@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    # menampilkan semua data buku
    books = Buku.objects.all()

    # melakukan filter contoh filter jumlah buku
    # books = Buku.objects.filter(jumlah=90)


    # iner joint( cara memanggil database yang berelasi(foreign key))
    # contoh iner joint kelompok_id (tambahkan __nama)
    # limit untuk menetukan banyaknya data yang tampil "[:2]" (tidak harus digunakan)
    # books = Buku.objects.filter(kelompok_id__nama='Produktif')[:2]

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


# CRUD "CREATE"
@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
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