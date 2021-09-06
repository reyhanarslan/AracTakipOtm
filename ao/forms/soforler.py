from django import forms
from ao.models import SoforModel, AracModel


class SoforForm(forms.ModelForm):
    class Meta:
        model = SoforModel
        fields =('sofor_adi','sofor_soyadi','arac_ilk_km','arac_son_km','arac_giris_saati','arac_cikis_saati')


