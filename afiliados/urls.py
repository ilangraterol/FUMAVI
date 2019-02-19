from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
	path('', admin.site.urls, name='admin_site'),
	path('afiliado', AfiliadoList.as_view(), name='list_afiliado'),
	path('afiliado/agregar', AfiliadoCreate.as_view(), name='crear_afiliado'),
	path('afiliado/<int:pk>/editar/', AfiliadoEdit.as_view(),  name='editar_afiliado'),
    path('afiliado/<int:pk>/eliminar/' , AfiliadoDelete.as_view(),  name='eliminar_afiliado'),

    path('pago', PagoList.as_view(), name='list_pago'),
	path('pago/agregar', PagoCreate.as_view(), name='crear_pago'),
	path('pago/<int:pk>/editar/', PagoEdit.as_view(),  name='editar_pago'),
    path('pago/<int:pk>/eliminar/' , PagoDelete.as_view(),  name='eliminar_pago'),
   
    
]


# CRUD - CREATE, READ, UPDATE, DELETE