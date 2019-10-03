from django.contrib import admin
from .models import *

class ProcedimientoInline(admin.TabularInline):
    model = Procedimiento
    extra = 1

class EspeInline(admin.TabularInline):
    model = Especialidad
    extra = 1

class EspecialidadInline(admin.TabularInline):
    model = Especialidad
    extra = 1

class AsesorInline(admin.TabularInline):
    model = Asesor
    extra = 1  
'''
class CentroMedicoInline(admin.TabularInline):
    model = CentroMedico
    extra = 1 
'''    

class ContratoAdmin(admin.ModelAdmin):         
	list_display = ('fechainicio', )
	inlines = [AsesorInline, EspecialidadInline, ProcedimientoInline ]
admin.site.register(Contrato, ContratoAdmin)


#admin.site.register(Especialidad)
admin.site.register(CentroMedico)
admin.site.register(Espe)

