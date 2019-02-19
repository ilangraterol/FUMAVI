from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *

class AfiliadoList(ListView):
    model = Afiliado
    template_name = 'lista_afiliados.html'
    def get_queryset(self):
        return Afiliado.objects.order_by('nombre')  

class AfiliadoCreate(CreateView):
    model = Afiliado
    form_class = RegistroAfiliado
    template_name = 'crear_afiliado.html'
    success_url = reverse_lazy('list_afiliado')  

class AfiliadoEdit(UpdateView):
    model = Afiliado
    form_class = RegistroAfiliado
    template_name = 'crear_afiliado.html'
    success_url = reverse_lazy('index_afiliado') 

class AfiliadoDelete(DeleteView):
    model = Afiliado
    template_name =  'afiliado_confirm_delete.html'
    success_url = reverse_lazy('index_afiliado')

class PagoList(ListView):
    model = Pago
    template_name = 'lista_pago.html'
    def get_queryset(self):
        return Pago.objects.order_by('fecha_pago')  

class PagoCreate(CreateView):
    model = Pago
    form_class = RegistroPago
    template_name = 'crear_pago.html'
    success_url = reverse_lazy('list_pago')  

class PagoEdit(UpdateView):
    model = Pago
    form_class = RegistroPago
    template_name = 'crear_pago.html'
    success_url = reverse_lazy('list_pago') 

class PagoDelete(DeleteView):
    model = Pago
    template_name =  'pago_confirm_delete.html'
    success_url = reverse_lazy('list_pago')





def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form})

def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form, 'product': product})

def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    return render(request, 'prod-delete-confirm.html', {'product': product})

