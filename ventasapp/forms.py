from django import forms
from django.forms import fields
from .models import Categoria
from .models import Cliente
from .models import Unidades as Unidad
from .models import Productos

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=['descripcion']

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['ruc_dni','nombres','apellidos','direccion', 'email', 'telefono']
    
class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ['descripcion']
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['descripcion','categoria','unidad','precio','cantidad']
        
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['unidad'].queryset = Unidad.objects.filter(estado=True)
        
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero")
        return precio
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad < 0:
            raise forms.ValidationError("La cantidad no puede ser negativa")
        return cantidad
