from django import forms
from .models import Equipo


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            'codigo_interno',
            'tipo_equipo',
            'marca',
            'serial',
            'ubicacion',
            'estado',
        ]
        widgets = {
            'codigo_interno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: EQ-001'}),
            'tipo_equipo': forms.Select(attrs={'class': 'form-select'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Dell, HP, Lenovo'}),
            'serial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de serie'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Aula 101, Oficina 3'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_codigo_interno(self):
        codigo = self.cleaned_data.get('codigo_interno')
        if not codigo or not codigo.strip():
            raise forms.ValidationError('El código interno no puede estar vacío.')
        return codigo.strip()

    def clean_serial(self):
        serial = self.cleaned_data.get('serial')
        if not serial or not serial.strip():
            raise forms.ValidationError('El serial no puede estar vacío.')
        return serial.strip()

    def clean_marca(self):
        marca = self.cleaned_data.get('marca')
        if not marca or not marca.strip():
            raise forms.ValidationError('La marca no puede estar vacía.')
        return marca.strip()

    def clean_ubicacion(self):
        ubicacion = self.cleaned_data.get('ubicacion')
        if not ubicacion or not ubicacion.strip():
            raise forms.ValidationError('La ubicación no puede estar vacía.')
        return ubicacion.strip()
