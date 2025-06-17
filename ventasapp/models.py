from django.db import models

# Create your models here.
class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=9)
    estado = models.BooleanField()
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
        
class Categoria(models.Model):
    descripcion = models.CharField(max_length=30)
    estado = models.BooleanField(default=True)
    
class Unidades(models.Model):
    descripcion = models.CharField(max_length=30)
    
class Productos(models.Model):
    descripcion = models.CharField(max_length=40)
    categorias=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    unidades = models.ForeignKey(Unidades, on_delete=models.CASCADE,null=True,blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    estado = models.BooleanField()
    
