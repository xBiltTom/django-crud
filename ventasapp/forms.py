from django import forms
from django.forms import fields
from .models import Categoria
from .models import Cliente
from .models import Unidades as Unidad

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=['descripcion','estado']

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['nombres', 'apellidos','direccion', 'email', 'telefono', 'estado']
    
class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ['descripcion']