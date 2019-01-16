from django.urls import path, include
from rest_framework import routers
from sena.models import *
from services.views import *

router.register(r'centros', centro_viewset)
router.register(r'eventos', evento_viewset)
router.register(r'categorias', categoria_viewset)

urlpatterns = [
	path('api/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),

]