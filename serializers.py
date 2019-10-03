from .models import *
from rest_framework import routers, serializers, viewsets

class AfiliadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afiliado
        fields = ('nombre', 'apellido', 'sexo', 'tipoDoc', 'documento')
        #fields = '__all__'

