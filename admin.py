from django.contrib import admin
from .models import *
from django.db.models import Sum

class PlanillaInline(admin.TabularInline):
    model = Planilla
    extra = 1

class FamiliaInline(admin.TabularInline):
    model = Familia
    extra = 1

class PagoInline(admin.TabularInline):
    model = Pago
    extra = 1

class PagoEmpresaInline(admin.TabularInline):
    model = PagoEmpresa
    extra = 1    

class EmpleadoInline(admin.TabularInline):
    model = Empleado
    extra = 1


class AfiliadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'servicios_afiliado', 'mensualidad', 'rango', 'documento','estatus', 'telefono','ciudad','departamento', )
    search_fields = ('nombre', 'apellido', 'documento')
    ordering = ('nombre',)
    filter_horizontal = ('servicios',) 
    list_filter = ('rango', 'estatus', 'ciudad') 
    list_per_page = 50
    fieldsets = [
        ('Informacion Personal',            {'fields': ['fecha_afiliacion','nombre','apellido', 'sexo', 'fecha_nacimiento', 'tipoDoc','documento',
                                             'prefijo', 'telefono', 'fijo','ciudad', 'departamento', 'direccion', 'email' ]}),
        ('Información Seguridad Social',    {'fields': ['rango', 'estatus', 'mensualidad', 'epsactual', 'epstraslado',
                                             'pinseguridadsocial', 'servicios' ]}),        
    ]    
    inlines = [PagoInline, PlanillaInline]
admin.site.register(Afiliado, AfiliadoAdmin)

   
class TipoServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', )
admin.site.register(TipoServicio, TipoServicioAdmin) 



class PagoAdmin(admin.ModelAdmin):
    	list_display = ('fecha_pago', 'afiliado', 'monto','recibo', 'observacion', )
    	search_fields = ('monto', 'afiliado__nombre', 'fecha_pago' ,'afiliado__apellido', 'afiliado__documento')
    	date_hierarchy = 'fecha_pago'
    	ordering = ('fecha_pago',)
    	raw_id_fields = ('afiliado',)
    	list_filter = ( 'fecha_pago', ) 
    	list_per_page = 30	

def changelist_view(self, request, extra_context=None):
    	total = Pago.objects.aggregate(total=Sum('monto'))['total']
    	context = {
    		'total': total,
    	}
    	return super(PagoAdmin, self).changelist_view(request, extra_context=context)

admin.site.register(Pago, PagoAdmin)


class EmpresaSeguridadSocialAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nombre',  'telefonos1', 'telefonos2','direccion','horario' )
    search_fields = ('nombre', )
    list_filter = ('tipo', ) 
    #search_fields = ('nombre', )
admin.site.register(EmpresaSeguridadSocial, EmpresaSeguridadSocialAdmin)

class EmpresaAfiliadaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nit',  'telefono', )
    search_fields = ('nombre', )
    list_filter = ('nombre', ) 
    inlines = [EmpleadoInline, PagoEmpresaInline]
admin.site.register(EmpresaAfiliada, EmpresaAfiliadaAdmin)


admin.site.register(TipoDocumento)
admin.site.register(Rango)


admin.site.register(Departamento)
admin.site.register(Ciudad)

admin.site.register(Vinculo)
admin.site.register(Familia)

admin.site.register(Año)


# Register your models here.
