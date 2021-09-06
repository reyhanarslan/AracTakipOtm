from django import forms
from ao.models import IletisimModel
class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel
        fields =('email','isim_soyisim','mesaj')

