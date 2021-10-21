from import_export import resources
from perpustakaan.models import Buku
from import_export.fields import Field

class BukuResource(resources.ModelResource):
    # untuk merubah nama
    kelompok_id__nama = Field(attribute='kelompok_id', column_name='kelompok')
    class Meta:
        model = Buku
        # untuk menentukan data apa saja yang diambil
        fields = ['judul', 'tanggal', 'kelompok_id__nama', 'penerbit', 'jumlah']
        # untuk mengurutkan
        export_order = ['judul', 'kelompok_id__nama', 'tanggal', 'penerbit', 'jumlah']