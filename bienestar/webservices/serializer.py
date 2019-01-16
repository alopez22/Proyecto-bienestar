from rest_framework import serializers
from sena.models import *

class centro_serializer(serializers.Serializer):
	class Meta:
		model = Centros
		fields = ('url','nombre','ubicacion','telefono',)

class evento_serializer(serializers.Serializer):
	class Meta:
		model = Eventos
		fields = ('url','nombre','descripcion','centros',)

class categoria_serializer(serializers.Serializer):
	class Meta:
		model = Categoria
		fields = ('url','nombre','descripcion','imagene',)