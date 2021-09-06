from django.contrib import admin
from ao.models import AracModel, SoforModel, MuayeneModel, IletisimModel, GuzergahModel
from ao.models.profil import ProfilModel


@admin.register(AracModel)
class AraclarAdmin(admin.ModelAdmin):

    search_fields = ('arac_marka','arac_adi')
    list_display = (
        'arac_marka','arac_adi','arac_model','arac_plaka'
    )
@admin.register(SoforModel)
class SoforlerAdmin(admin.ModelAdmin):
    search_fields = ('sofor_adi','sofor_soyadi')
    list_display = (
        'sofor_id','sofor_adi','sofor_soyadi'
    )
@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    search_fields = ('email','isim_soyisim','olusturulma_tarihi')
    list_display = (
        'isim_soyisim','email','mesaj','olusturulma_tarihi'
    )
admin.site.register(MuayeneModel)
admin.site.register(GuzergahModel)
admin.site.register(ProfilModel)
# Register your models he