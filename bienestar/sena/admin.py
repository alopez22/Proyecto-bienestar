from django.contrib import admin

from .models import *

# Register your models here.
#Desde aqui podemos "registrar" nuestros modelos para que luego se creen en la base de datos
#Una vez creados los modelos ejecutamos el comando "python manage.py makemigrations" para que nos reconozca los modelos o cambios a migrar.
#finalmente con el comando migrate hacemos las migraciones, lo que hace que se apliquen y envíen los cambios y ajustes a la base de datos.
admin.site.register(Centros)
admin.site.register(Eventos)
admin.site.register(Categoria)
admin.site.register(Tips)
admin.site.register(Perfil)