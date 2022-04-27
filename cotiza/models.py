from django.db import models

# Create your models here.

class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    cliente_nombre = models.CharField(max_length=50)
    cliente_rut = models.CharField(max_length=20, unique=True)
    cliente_direccion = models.CharField(max_length=100)
    cliente_ciudad = models.CharField(max_length=30)
    cliente_provincia = models.CharField(max_length=30)
    cliente_pais = models.CharField(max_length=20)
    cliente_telefono = models.CharField(max_length=12)
    cliente_email = models.EmailField(max_length=60)
    cliente__web = models.URLField(max_length=50)
    cliente_fechaIngreso = models.DateTimeField(auto_now_add=True)
    
class Contacto_cliente(models.Model):
    contacto_cliente_id = models.AutoField(primary_key=True)
    contacto_nombre = models.CharField(max_length=50)
    contacto_apellido = models.CharField(max_length=60)
    contacto_email = models.EmailField(max_length=60)
    contacto_celular = models.CharField(max_length=12)
    contacto_cargo = models.CharField(max_length=40)
    contacto_cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
# class Cliente_cotizacion(models.Model):
#     cotizacion_id = models.AutoField(primary_key=True)
#     fecha_cotizacion = models.DateField(auto_now=True)
#     tipo_cotizacion = models.CharField(max_length=45)
#     responsable = models.CharField(max_length=50)
#     cliente_principal = models.CharField(max_length=50)
#     cliente_final = models.CharField(max_length=50)
#     descripcion = models.TextField()
#     observaciones = models.TextField()
#     clientes_cliente_cotiza = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    
    
    
    
    
    
    