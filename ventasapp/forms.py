from django import forms
from django.forms import fields
from .models import Categoria, Cliente, Productos, Tipo, Parametros, cabeceraVentas, detalleVentas
from .models import Unidades as Unidad

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field
from datetime import date


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
        self.fields['categoria'].queryset = Categoria.objects.filter(estado=True)
        
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

class VentaForm(forms.Form):
    fecha_venta = forms.DateField(
        label = "Fecha",
        
        widget = forms.TextInput(attrs={'class': 'form-control text-center', 'autocomplete':'off', 'id' : 'id_fecha_venta'}),
        input_formats = ['%d/%m/%Y', '%Y-%m-%d'], 
    )

    tipo = forms.ModelChoiceField(
        queryset=Tipo.objects.all(),
        label="Tipo Documento",
        empty_label= "- Seleccione Tipo -",
        widget= forms.Select(attrs = {'class': 'form-control', 'onchange': 'obtenerDatosTipoDocumento()', 'id': 'id_tipo_documento'}),
        
    )

    nrodoc = forms.CharField(
        label = "Nro. Documento",
        required = False, 
        widget = forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'id' : 'id_nrodoc' })
    )
    
    cliente = forms.ModelChoiceField (
        queryset=Cliente.objects.filter(estado=True),
        label="Cliente",
        empty_label="- Seleccione Cliente -",
        widget = forms.Select(attrs={'class': 'form-control', 'onchange': 'obtenerDatosCliente()', 'id': 'id_cliente_venta'}),
    )

    ruc_dni = forms.CharField (
        label= "RUC/DNI",
        required=False, 
        widget= forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'id': 'id_ruc_dni_cliente'})
    )

    direccion = forms.CharField (
        label= "Dirección",
        required= False,
        widget= forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'id': 'id_direccion_cliente'}) # Corregido 'readonnly' a 'readonly'
    )

    
    producto_seleccionado = forms.ModelChoiceField (
        queryset=Productos.objects.filter(estado=True, cantidad__gt= 0 ),
        label= "Producto",
        empty_label= "-- Seleccione Producto --",
        widget=forms.Select(attrs={'class': 'form-control', 'onchange': 'obtenerDatosProducto()', 'id': 'id_producto_seleccionado'}),
        required=False 
    )

    unidad_producto = forms.CharField(
        label="Unidad",
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'id': 'id_unidad_producto'})
    )

    precio_producto = forms.DecimalField(
        label="Precio",
        required=False, 
        max_digits=10,
        decimal_places=2,
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'id': 'id_precio_producto'}) 
    )

    cantidad_producto = forms.IntegerField(
        label="Cantidad",
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'oninput': 'calcularImporteProductoActual()', 'id': 'id_cantidad_producto'}), # onchange a oninput
        required=False 
    )

    stock_disponible = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput(attrs={'id': 'id_stock_disponible'})
    )

    total = forms.DecimalField (
        label= 'Total S/.',
        required=False,
        max_digits=10,
        decimal_places=2,
        widget=forms.TextInput(attrs={'class':'form-control text-right', 'readonly': 'readonly', 'id': 'id_total_venta'})
    )

    subtotal = forms.DecimalField(
        required=False,
        max_digits=10,
        decimal_places=2,
        widget=forms.HiddenInput(attrs={'id':'id_subtotal_venta'})
    )

    igv = forms.DecimalField(
        required=False,
        max_digits=10,
        decimal_places=2,
        widget = forms.HiddenInput(attrs={'id':'id_igv_venta'}) 
    )

    def __init__(self, *args, **kwargs) :
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout (
            Row(
                Column('fecha_venta',css_class='form-group col-md-3'),
                Column('tipo',css_class='form-group col-md-3' ),
                Column('nrodoc',css_class='form-group col-md-3'),
                css_class = 'form-row align-items-end'
            ),
            Row(
                Column('cliente', css_class='form-group col-md-6'),
                Column('ruc_dni',css_class='form-group col-md-3'),
                Column('direccion',css_class='form-group col-md-3'),
                css_class='form-row'
            ),
            Row(
                Column('producto_seleccionado',css_class='form-group col-md-6'),
                Column('unidad_producto',css_class='form-group col-md-2'),
                Column('precio_producto',css_class='form-group col-md-2'),
                Column('cantidad_producto',css_class='form-group col-md-2'),
                css_class='form-row'
            ),
            Field('stock_disponible',type = "hidden"),
        )

class DetalleVentaForm(forms.Form):
        producto_id = forms.IntegerField()
        precio = forms.DecimalField(max_digits=10, decimal_places=2)
        cantidad = forms.IntegerField()
        importe = forms.DecimalField(max_digits=10, decimal_places=2)