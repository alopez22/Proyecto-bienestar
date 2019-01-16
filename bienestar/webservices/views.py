from sena.models import *
from .serializer import *
from rest_framework import *

# Create your views here.

class centro_viewset(viewsets.ModelViewset):
	queryset = Centros.objects.all()
	serializer_class = centro_serializer


class evento_viewset(viewsets.ModelViewset):
	queryset = Eventos.objects.all()
	serializer_class = evento_serializer

class categoria_viewset(viewsets.ModelViewset):
	queryset = Categoria.objects.all()
	serializer_class = categoria_serializer
