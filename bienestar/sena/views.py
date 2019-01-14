#Importamos la funcion redirect, para poder reenviar al usuario a otra página o documento tras una acción.
from django.shortcuts import render, redirect
#Importamos todos los formularios con el simbolo *
from .forms import *
#Importamos todos nuestros modelos
from .models import *
#Importamos las variables de autenticación de la libreria
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 
# Create your views here.
#Creamos las funciones con las vistas, que nos recogeran la información de los formularios y modelos etc.
def vista_lista_sustancias(request):
	#Le indicamos a esta vista que recoga los datos del modelo categoría y los filtre
	lista = Categoria.objects.filter()
	#Luego le especificamos a que template nos redirigirá dicha información.
	return render(request, 'lista_sustancias.html', locals())

#Creamos nuestra vista que nos recogerá el id de cada item del modelo categoría
def vista_ver_droga(request, id_category):
	#Obtenemos el id de cada item, que por lo general empieza en 0 o en 1
	c = Categoria.objects.get(id=id_category)
	#Le indicamos que nos regrese los datos al template de ver droga, para una información detallada.
	return render(request, 'ver_droga.html', locals())

#Vista que nos permitirá editar los campos de un item previamente agregado.
def vista_editar_droga(request, id_category):
	#Obtenemos el id del item que se editará
	cate = Categoria.objects.get(id = id_category)
	#Creamos una condición con el método POST, para gestionar la información de un item de la tabla categoría
	if request.method =="POST":
		formulario = agregar_categoria_form(request.POST, request.FILES, instance =cate)
		if formulario.is_valid():
			#Una ves editados los campos del item que haya seleccionado el usuario, le indicamos al formulario que guarde los cambios.
			cate = formulario.save()
			#Función que nos regresa al template que contiene la lista de los datos ya modificados.
			return redirect('/lista_sustancias')
	#Si no se cumple la petición de forma correcta, nos regresará al template de agregar una sustancia.
	else:
		formulario = agregar_categoria_form(instance = cate)
		return render(request, 'agregar_sustancia_psicoactiva.html', locals())

#Vista que dará la opción de eliminar un item de la tabla Categoría al superusuario.
def vista_eliminar_droga(request, id_category):
	cate = Categoria.objects.get(id = id_category)
	cate.delete()
	return redirect('/lista_sustancias/')

#Vista que dará la opción de agregar una droga a la tabla categoría al superusuario.
def vista_agregar_sustancia_psicoactiva(request):
	if request.method == 'POST':
		formulario = agregar_categoria_form(request.POST, request.FILES)
		if formulario.is_valid():
		   cate = formulario.save(commit = False)
		   cate.status = True
		   #Variable que nos guarda los cambios a la tabla
		   cate.save()
		   formulario.save_m2m()
		   #Variable que nos regresa al template de lista con los items.
		return redirect('/lista_sustancias/')
	#Si no se cumple la condición anterior, entonces nos retorna al template de agregar la sustancia.
	else:
		formulario = agregar_categoria_form()
	return render(request, 'agregar_sustancia_psicoactiva.html', locals())

#Vista que nos recoge los datos del usuario para loguearse en la aplicación.
def vista_login(request):
	usu = ""
	cla = ""
	if request.method == "POST":
		formulario = login_form(request.POST)
		if formulario.is_valid():
			#Si la información es válida se limpiarán las cajas de usuario y contraseña
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['contraseña']
			usuario = authenticate(username=usu, password=cla)

			#Si el usuario no existe pero sigue en la aplicación, se le pedirá iniciar sesión
			if usuario is not None and usuario.is_active:
			   login(request, usuario)
			   #Función que redirecciona al usuario a la página principal
			   return redirect('/')
			   #Si no se cumple correctamente el requisito en el formulario, se le enviará un mensaje al usuario.
			else:
				msj = "usuario o clave incorrectos"
	formulario = login_form()
	#Será redireccionado al template de iniciar sesión.
	return render(request, 'login.html', locals())

#Vista que cierra la sesión del usuario y lo regresa a la página de inicio de sesón.
def vista_logout(request):
	logout(request)
	return redirect('/login/')

#Vista para nuestro template de inicio.
def vista_inicio(request):
	return render(request, 'inicio.html', locals())

def vista_register(request):
	formulario = register_form()
	if request.method == 'POST':
		formulario = register_form(request.POST)
		if formulario.is_valid():
			usuario = formulario.cleaned_data['username']
			correo = formulario.cleaned_data['email']
			password_1 = formulario.cleaned_data['password_1']
			password_2 = formulario.cleaned_data['password_2']
			u = User.objects.create_user(username=usuario, email=correo, password= password_1)
			u.save()
			return render(request, 'thanks_for_register.html', locals())
		else:
			return render(request, 'register.html', locals())
	return render(request, 'register.html', locals())



def vista_crear_perfil(request):
	formulario_1 = register_form()
	formulario_2 = perfil_form()
	if request.method == 'POST':
		formulario_1 = register_form(request.POST)
		formulario_2 = perfil_form(request.POST, request.FILES)
		if formulario_1.is_valid() and formulario_2.is_valid():
			usuario = formulario_1.cleaned_data['username']
			correo = formulario_1.cleaned_data['email']
			password_1 = formulario_1.cleaned_data['password_1']
			password_2 = formulario_1.cleaned_data['password_2']
			u = User.objects.create_user(username=usuario, email=correo, password= password_1)
			u.save()
			
			y = formulario_2.save(commit = False)
			y.user = u
			y.save()
	return render(request, 'crear_perfil.html', locals())
#Vista que nos recoge los items del Modelo Tips para luego listarlos en nuestra aplicación.
def vista_lista_tips(request):
	lista2 = Tips.objects.filter()
	#Enviamos los datos a peticion a nuestro template que tendrá la lista con los datos.
	return render(request, 'lista_tips.html', locals())

#Vista que nos recoge los datos del modelo Centros para luego mostrarlos al Aprendiz o usuario.
def vista_ver_centros(request):
	lista3 = Centros.objects.filter()
	#Enviamos esos datos a nuestro template asignado para mostrarlos al usuario.
	return render(request, 'lista_ver_centros.html', locals())

def vista_agregar_centro(request):
	if request.method == 'POST':
		formulario = agregar_centro_form(request.POST, request.FILES)
		if formulario.is_valid():
		   cent = formulario.save(commit = False)
		   cent.status = True
		   #Variable que nos guarda los cambios a la tabla
		   cent.save()
		   formulario.save_m2m()
		   #Variable que nos regresa al template de lista con los items.
		return redirect('/lista_ver_centros/')
	#Si no se cumple la condición anterior, entonces nos retorna al template de agregar la sustancia.
	else:
		formulario = agregar_centro_form()
	return render(request, 'agregar_centro.html', locals())


#Vista que nos permitirá editar los campos de un item previamente agregado.
def vista_editar_centros(request, id_center):
	#Obtenemos el id del item que se editará
	cent = Centros.objects.get(id = id_center)
	#Creamos una condición con el método POST, para gestionar la información de un item de la tabla categoría
	if request.method =="POST":
		formulario = agregar_centro_form(request.POST, request.FILES, instance =cent)
		if formulario.is_valid():
			#Una ves editados los campos del item que haya seleccionado el usuario, le indicamos al formulario que guarde los cambios.
			cent = formulario.save()
			#Función que nos regresa al template que contiene la lista de los datos ya modificados.
			return redirect('/lista_ver_centros')
	#Si no se cumple la petición de forma correcta, nos regresará al template de agregar una sustancia.
	else:
		formulario = agregar_centro_form(instance = cent)
		return render(request, 'agregar_centro.html', locals())

#Vista que dará la opción de eliminar un item de la tabla Categoría al superusuario.
def vista_eliminar_centros(request, id_center):
	cent = Centros.objects.get(id = id_center)
	cent.delete()
	return redirect('/lista_ver_centros/')

def vista_lista_eventos(request):
	lista4 = Eventos.objects.filter()
	#Enviamos los datos a peticion a nuestro template que tendrá la lista con los datos.
	return render(request, 'lista_eventos.html', locals())


def vista_agregar_eventos(request):
	if request.method == 'POST':
		formulario = agregar_eventos_form(request.POST, request.FILES)
		if formulario.is_valid():
		   event = formulario.save(commit = False)
		   event.status = True
		   #Variable que nos guarda los cambios a la tabla
		   event.save()
		   formulario.save_m2m()
		   #Variable que nos regresa al template de lista con los items.
		return redirect('/lista_eventos/')
	#Si no se cumple la condición anterior, entonces nos retorna al template de agregar la sustancia.
	else:
		formulario = agregar_eventos_form()
	return render(request, 'agregar_eventos.html', locals())


def vista_editar_eventos(request, id_events):
	#Obtenemos el id del item que se editará
	event = Eventos.objects.get(id = id_events)
	#Creamos una condición con el método POST, para gestionar la información de un item de la tabla categoría
	if request.method =="POST":
		formulario = agregar_eventos_form(request.POST, request.FILES, instance =event)
		if formulario.is_valid():
			#Una ves editados los campos del item que haya seleccionado el usuario, le indicamos al formulario que guarde los cambios.
			event = formulario.save()
			#Función que nos regresa al template que contiene la lista de los datos ya modificados.
			return redirect('/lista_eventos')
	#Si no se cumple la petición de forma correcta, nos regresará al template de agregar una sustancia.
	else:
		formulario = agregar_eventos_form(instance = event)
		return render(request, 'agregar_eventos.html', locals())

#Vista que dará la opción de eliminar un item de la tabla Categoría al superusuario.
def vista_eliminar_eventos(request, id_events):
	event = Eventos.objects.get(id = id_events)
	event.delete()
	return redirect('/lista_eventos/')
