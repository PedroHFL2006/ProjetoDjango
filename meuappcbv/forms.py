from django import forms
from.models import ViaCep

class ViaCepForm(forms.ModelForm):
    class Meta:
        model = ViaCep
        fields =['cep']
        widgets ={
                'cep': forms.TexImput(attrs={'placeholder': 'Digite o CEP', 
                'class': 'form-control'})
        }
        labels = {
            'cep': 'CEP'
        }