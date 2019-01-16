from django.urls import path
#importamos desde el views.py todas las vistas a enlazar con nuestras url.
from .views import *
#Importamos la autenticación para nuestros templates de inicio y cierre de sesión.
from django.contrib.auth.models import User 

#Creamos el nombre que le asignaremos a nuestro template y a nuestras vistas asociadas.
#También creamos una función especifica que nos recogerá el id de nuestros items de la lista de sustancias y demás.
urlpatterns = [
	path('',vista_inicio),
	path('agregar_sustancia_psicoactiva/',vista_agregar_sustancia_psicoactiva, name='vista_agregar_sustancia_psicoactiva'),
	path('lista_sustancias/', vista_lista_sustancias, name='vista_lista_sustancias'),
	path('ver_droga/<int:id_category>/', vista_ver_droga, name='vista_ver_droga' ),
	path('editar_droga/<int:id_category>/', vista_editar_droga, name='vista_editar_droga' ),
	path('eliminar_droga/<int:id_category>/', vista_eliminar_droga, name='vista_eliminar_droga' ),
	path('login/',vista_login, name ='vista_login'),
	path('logout/',vista_logout, name ='vista_logout'),
	path('crear_perfil/',vista_crear_perfil, name= 'crear_perfil'),
	path('lista_tips/',vista_lista_tips, name='vista_lista_tips'),
	path('lista_ver_centros/', vista_ver_centros, name='vista_ver_centros'),
	path('editar_centros/<int:id_center>/', vista_editar_centros, name='vista_editar_centros' ),
	path('eliminar_centros/<int:id_center>/', vista_eliminar_centros, name='vista_eliminar_centros' ),
	path('agregar_centro/',vista_agregar_centro, name='vista_agregar_centro'),
	path('editar_eventos/<int:id_events>/', vista_editar_eventos, name='vista_editar_eventos' ),
	path('eliminar_eventos/<int:id_events>/', vista_eliminar_eventos, name='vista_eliminar_eventos' ),
	path('agregar_eventos/',vista_agregar_eventos, name='vista_agregar_eventos'),
	path('lista_eventos/',vista_lista_eventos, name='vista_lista_eventos'),
	path('editar_tips/<int:id_typis>/', vista_editar_tips, name='vista_editar_tips' ),
	path('eliminar_tips/<int:id_typis>/', vista_eliminar_tips, name='vista_eliminar_tips' ),
	path('agregar_tips/',vista_agregar_tips, name='vista_agregar_tips'),
]