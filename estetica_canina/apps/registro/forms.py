from django import forms
from .models import Cita


class CitasForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombre', 'descripcion', 'fecha_cita'] 

        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion de Servicio',
            'fecha_cita': 'Fecha de la cita',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_cita': forms.DateInput(attrs={'class': 'form-control'}),
        }
