from django import forms
from library.models import Kitob



class Kitob_form(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = ["nom", "sahifa", "tur"]
