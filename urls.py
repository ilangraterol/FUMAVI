from django.contrib import admin
from django.urls import path, include
from .views import*
from django.views.generic import TemplateView


urlpatterns = [
	
	
	
	
	#path('APIafiliado', ApiAfiliadoList.as_view(), name='list_afiliado'),
	#path('APIafiliado/<int:pk>/', ApiAfiliadoDetail.as_view(),  name='detalle'),


	path('', AfiliadoList.as_view(), name='lista_afiliados'),
	path('afiliado', AfiliadoList.as_view(), name='lista_afiliados'),
	path('afiliador', AfiliadoListRetirados.as_view(), name='list_afiliado_retirados'),
	path('afiliadon', AfiliadoListNivelados.as_view(), name='list_afiliado_nivelados'),
	path('afiliadoo', AfiliadoListOrdenados.as_view(), name='list_afiliado_ordenados'),
	path('afiliado/<int:pk>/', DetalleAfiliados.as_view(), name='detail'),
	path('afiliado/agregar', AfiliadoCreate.as_view(), name='crear_afiliado'),
	path('afiliado/<int:pk>/editar/', AfiliadoEdit.as_view(),  name='editar_afiliado'),
    path('afiliado/<int:pk>/eliminar/' , AfiliadoDelete.as_view(),  name='eliminar_afiliado'),

    path('empresa', EmpresaList.as_view(), name='lista_empresas'),
    path('empresa/agregar', EmpresaCreate.as_view(), name='crear_empresa'),
    path('empresa/<int:pk>/', DetalleEmpresa.as_view(), name='detalle_empresa'),
    path('empresa/<int:pk>/editar/', EmpresaEdit.as_view(),  name='editar_empresa'),
    path('empresa/<int:pk>/eliminar/' , EmpresaDelete.as_view(),  name='eliminar_empresa'),

    path('pago', PagoList.as_view(), name='lista_pagos'),
	path('pago/agregar', PagoCreate.as_view(), name='crear_pago'),
	path('pago/<int:pk>/editar/', PagoEdit.as_view(),  name='editar_pago'),
    path('pago/<int:pk>/eliminar/' , PagoDelete.as_view(),  name='eliminar_pago'),
   
    
]


# CRUD - CREATE, READ, UPDATE, DELETE