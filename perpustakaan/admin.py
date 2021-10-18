from django.contrib import admin
from perpustakaan.models import Buku, Kelompok
# Register your models here.

# membuat display tampilan di admin
# selengkapnya dapat dilihat di https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#modeladmin-options


class BukuAdmin(admin.ModelAdmin):
    # untuk menampilkan list (disini kita dapat menampilkan tabel)
    list_display = ['judul', 'penulis', 'penerbit', 'jumlah', 'kelompok_id']
    # untuk menampilkan menu percarian
    search_fields = ['judul', 'penulis', 'penerbit']
    # untuk membuat filter
    list_filter = ['kelompok_id']
    # jumlah list data per page
    list_per_page = 5


# menampilkan data buku dan kelompok (jangan lupa menambahkan kelas BukuAdmin)
admin.site.register(Buku, BukuAdmin)
admin.site.register(Kelompok)
