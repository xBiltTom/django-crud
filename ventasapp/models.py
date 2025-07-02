from django.db import models
from django.db.models import Sum, F
from django.db import transaction



# Create your models here.
class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    ruc_dni = models.CharField(max_length=11,null=True,blank=True)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=9)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
        
class Categoria(models.Model):
    descripcion = models.CharField(max_length=30)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.descripcion}"
    
class Unidades(models.Model):
    descripcion = models.CharField(max_length=30)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.descripcion}"
    
class Productos(models.Model):
    descripcion = models.CharField(max_length=40)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidades, on_delete=models.CASCADE,null=True,blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
    
    @classmethod
    def actualizar_stock(cls,producto_id,cantidad_vendida):
        try:
            producto = cls.objects.get(pk=producto_id)
            if producto.cantidad >= cantidad_vendida:
                producto.cantidad = F('cantidad') - cantidad_vendida
                producto.save()
                return True
            else:
                return False
        except cls.DoesNotExist:
            return False 
    
class Tipo(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion
    
class Parametros(models.Model):
    tipo_id = models.OneToOneField(Tipo, on_delete=models.CASCADE,primary_key=True)
    numeracion = models.CharField(max_length=8)
    serie = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.tipo_id.descripcion} - Serie: {self.serie}. Nro: {self.numeracion}"
    
    @classmethod
    def actualizar_numeracion(cls, tipo_id):
        with transaction.atomic():
            parametro = cls.objects.select_for_update().get(tipo_id=tipo_id)
            numero_actual = int(parametro.numeracion)
            parametro.numeracion = str(numero_actual + 1).zfill(len(parametro.numeracion))
            parametro.save()
            return f"{parametro.serie}-{parametro.numeracion}"

class cabeceraVentas(models.Model):
    venta_id = models.AutoField(primary_key=True)
    cliente_id = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    fecha_venta = models.DateField()
    tipo_id = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    nrodoc = models.CharField(max_length=13)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    igv = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta {self.nrodoc} - {self.cliente_id.nombres} - {self.fecha_venta}"
    
class detalleVentas(models.Model):
    venta_id = models.ForeignKey(cabeceraVentas, on_delete=models.CASCADE,related_name="detalles")
    producto_id = models.ForeignKey(Productos, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    importe = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Detalle de Venta {self.venta_id.nrodoc} - {self.producto_id.descripcion} ({self.cantidad})" 
    