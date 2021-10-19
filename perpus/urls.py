from django.contrib import admin
from django.urls import path
# * digunakan untuk import semua
from perpustakaan.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku, name='buku'),
    path('penerbit/', penerbit, name='penerbit'),
    path('tambah-buku/', tambah_buku, name='tambah_buku'),
    # untuk path ubah buku agak berbeda
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name='hapus_buku'),    
]

# NOTE
# jangan lupa tambah views setiap membuat path
