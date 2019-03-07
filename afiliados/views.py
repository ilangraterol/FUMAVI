from django.urls import reverse_lazy

from .forms import *
from afiliados.models import *
from notificaciones.models import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

import datetime
from django.views import generic


        #rest framework 
from .serializers import AfiliadoSerializer
from rest_framework import generics

class DetalleAfiliados(DetailView):
    model = Afiliado  
    template_name = 'detalle_afiliado.html'

    def get_context_data(self, *args, **kwargs):
         # El pk que pasas a la URL
        pk = self.kwargs.get('pk')
        afiliados = Afiliado.objects.filter(id=pk)
        pagos = Pago.objects.filter(afiliado_id=pk).order_by('-fecha_pago')[:5]               
        return {'afiliados': afiliados, 'pagos': pagos}          


class DetalleEmpresa(DetailView):
    model = Pago  
    template_name = 'detalle_empresa.html'

    def get_context_data(self, *args, **kwargs):
         # El pk que pasas a la URL
        pk = self.kwargs.get('pk')
        afiliados = EmpresaAfiliada.objects.filter(id=pk)
        pagos = Pago.objects.filter(afiliado_id=pk).order_by('-fecha_pago')[:5]               
        return {'afiliados': afiliados, 'pagos': pagos}          

class AfiliadoList(ListView):
    model = Afiliado       
    template_name = 'lista_afiliados.html'    

    def get_context_data(self, *args, **kwargs): 
        lista_afiliados = Afiliado.objects.filter(estatus=1).order_by('nombre') 
        mensaje = Notificaciones.objects.filter(tipo="Cobro") 
        conteo = Afiliado.objects.filter(estatus=1).count()       
        return { 'lista_afiliados': lista_afiliados, 'mensaje': mensaje, 'conteo':conteo}     

class AfiliadoListRetirados(AfiliadoList):
    template_name = 'lista_afiliados_retirados.html'
    
    def get_context_data(self, *args, **kwargs):    
        lista_retirados = Afiliado.objects.filter(estatus=0).order_by('nombre') 
        mensaje = Notificaciones.objects.filter(tipo="Cobro")              
        return { 'lista_retirados': lista_retirados, 'mensaje' : mensaje }                  


class AfiliadoCreate(CreateView):
    model = Afiliado
    form_class = RegistroAfiliado
    template_name = 'crear_afiliado.html'
    success_url = reverse_lazy('lista_afiliados')          

class AfiliadoEdit(UpdateView):
    model = Afiliado
    form_class = RegistroAfiliado
    template_name = 'crear_afiliado.html'
    success_url = reverse_lazy('lista_afiliados')     

class AfiliadoDelete(DeleteView):
    model = Afiliado
    template_name =  'borrar_afiliado.html'
    success_url = reverse_lazy('lista_afiliados')      

class EmpresaList(ListView):
    model = EmpresaAfiliada  
    second_model = Notificaciones  
    template_name = 'lista_empresas.html'    

    def get_context_data(self, *args, **kwargs):    
        lista_empresas = EmpresaAfiliada.objects.all().order_by('nombre') 
        mensaje = Notificaciones.objects.filter(tipo='Empresas')                
        return { 'lista_empresas': lista_empresas, 'mensaje': mensaje}             

class EmpresaCreate(CreateView):
    model = EmpresaAfiliada
    form_class = RegistroEmpresa
    template_name = 'crear_empresa.html'
    success_url = reverse_lazy('lista_empresas')          

class EmpresaEdit(UpdateView):
    model = EmpresaAfiliada
    form_class = RegistroEmpresa
    template_name = 'crear_empresa.html'
    success_url = reverse_lazy('lista_empresas')         

class EmpresaDelete(DeleteView):
    model = EmpresaAfiliada
    template_name =  'borrar_empresa.html'
    success_url = reverse_lazy('lista_empresas') 






class ApiAfiliadoList(generics.ListCreateAPIView):
    queryset = Afiliado.objects.all()
    serializer_class = AfiliadoSerializer

class ApiAfiliadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Afiliado.objects.all()
    serializer_class = AfiliadoSerializer


class PagoList(ListView):
    model = Pago
    template_name = 'lista_pago.html'
    context_object_name = 'lista_pagos'
    paginate_by = 10
    def get_queryset(self):
        return Pago.objects.order_by('-fecha_pago')  

class PagoCreate(CreateView):
    model = Pago
    form_class = RegistroPago
    template_name = 'crear_pago.html'

    success_url = reverse_lazy('lista_pagos')  

class PagoEdit(UpdateView):
    model = Pago
    form_class = RegistroPago
    template_name = 'crear_pago.html'
    success_url = reverse_lazy('lista_pagos') 

class PagoDelete(DeleteView):
    model = Pago
    template_name =  'borrar_pago.html'
    success_url = reverse_lazy('lista_pagos')




