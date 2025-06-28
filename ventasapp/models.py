from django.db import models

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
    
class Tipo(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    
class Parametros(models.Model):
    tipo_id = models.OneToOneField(Tipo, on_delete=models.CASCADE,primary_key=True)
    numeracion = models.CharField(max_length=15)
    serie = models.CharField(max_length=3)
    
class cabeceraVentas(models.Model):
    venta_id = models.AutoField(primary_key=True)
    cliente_id = models.OneToOneField(Cliente,on_delete=models.CASCADE)
    fecha_venta = models.DateField()
    tipo_id = models.OneToOneField(Tipo,on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    nrodoc = models.CharField(max_length=12)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    igv = models.DecimalField(max_digits=10, decimal_places=2)
    
class detalleVentas(models.Model):
    venta_id = models.OneToOneField(cabeceraVentas, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Productos, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    
    