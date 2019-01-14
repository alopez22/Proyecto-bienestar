from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
# Creamos nuestros modelos para la base de datos
class Centros(models.Model):
	nombre	=models.CharField(max_length = 100)
	ubicacion = models.CharField(max_length = 200)
	telefono = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

#Estos modelos se crearan en nuestra base de datos sqlite3
class Eventos(models.Model):
	#Especificamos el nombre de cada campo y le asignamos el tipo de dato que recogerá
	nombre	= models.CharField(max_length = 100)
	descripcion	= models.TextField(max_length = 500)
	#Enlazamos nuestro modelo con el de Centros, para así poder escoger un centro asociado al evento
	centros	= models.ForeignKey(Centros, on_delete = models.PROTECT)

#Utilizamos una función para que nos regrese el dato de nuestro modelo
# La función recoge todos los datos en formato STR o "String"
	def __str__(self):
		return self.nombre

#Creamos el modelo para los tipos de sustancias psicoactivas, con los campos y su tipo de dato:
class Categoria(models.Model):
	nombre	= models.CharField(max_length = 100)
	descripcion	= models.TextField(max_length = 500)

	#Creamos un objeto de tipo ImageField, para poder mostrar imágenes de las sustancias psicoactivas.
	#Con la función upload enviamos dichas imagenes a una carpeta, a la que nombraremos entre comillas simples.
	imagene = models.ImageField(upload_to='sustancias', null = True, blank = True)
	

	def __str__(self):
		return self.nombre


class Tips(models.Model):
	nombre =models.CharField(max_length = 100)
	descripcion = models.TextField(max_length= 600)
	
	def __str__(self):
		return self.nombre

class Perfil(models.Model):
	documento = models.CharField(max_length = 20)
	edad = models.IntegerField()
	telefono = models.CharField(max_length = 50)
	imagen = models.ImageField(upload_to='perfiles', null = True, blank = True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.documento
