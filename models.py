from django.db import models
from django.utils import timezone
import datetime


class Mes(models.Model):
    nombre = models.CharField(max_length=50, unique=True)    
    def __str__(self):
        cadena = "{0} "
        return cadena.format(self.nombre) 

class Año(models.Model):
    nombre = models.IntegerField(unique=True)    
    def __str__(self):
        cadena = "{0} "
        return cadena.format(self.nombre)             

class Departamento(models.Model):
    nombre = models.CharField(max_length=50, unique=True)    
    def __str__(self):
        cadena = "{0} "
        return cadena.format(self.nombre)      

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)    
    def __str__(self):
        cadena = "{0} "
        return cadena.format(self.nombre) 

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Ciudades"                 

class Rango(models.Model):
    nombre = models.CharField(max_length=50)    
    def __str__(self):
        cadena = "{0} "
        return cadena.format(self.nombre)         

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50)    
    def __str__(self):
        cadena = "{0} "
        return cadena.format(self.nombre)                 

class TipoServicio(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(blank=True, null = True)

    def __str__(self):
        cadena = "{0} "
        return cadena.format(self.nombre) 

class EmpresaSeguridadSocial(models.Model):
    tipo = models.ForeignKey(TipoServicio, null = False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    telefonos1 = models.CharField(max_length=50, blank=True, verbose_name='telefono (Fijo)')
    telefonos2 = models.CharField(max_length=50, blank=True, verbose_name='telefono (Opcional)') 
    direccion = models.CharField(max_length=200, blank=True)
    horario = models.CharField(max_length=70, blank=True, verbose_name='Horario de Atencion')
    nombreasesor = models.CharField(max_length=50, blank=True, verbose_name='Nombre del Asesor')
    telefonoAsesor  = models.CharField(max_length=50, blank=True, verbose_name='Telefono del Asesor')

    def __str__(self):
        cadena = "{0} "
        return cadena.format(self.nombre) 

    class Meta:
        #ordering = ["nombre"]
        verbose_name_plural = "Empresas Seguridad Social"      

class Vinculo(models.Model): 
    nombre = models.CharField(max_length=50, unique=True) 
    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.nombre)              

class Afiliado(models.Model):
    fecha_afiliacion = models.DateField(null=True, blank=True)    
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50)    
    sexo = models.CharField(max_length=12, blank=True, choices=(('M', 'Masculino'), ('F', 'Femenino'),))
    fecha_nacimiento = models.DateField(null=True, blank=True) 
    tipoDoc = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, verbose_name='Tipo de Documento')      
    documento = models.CharField(max_length=50, unique=True)
    mensualidad = models.FloatField(blank=True, null = True)
    rango = models.ForeignKey(Rango, blank=True, null = True, on_delete=models.CASCADE)     
    servicios = models.ManyToManyField(TipoServicio, blank=True, verbose_name='servicios') 
    ciudad = models.ForeignKey(Ciudad, blank=True, null = True, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, blank=True, null = True, on_delete=models.CASCADE)     
    distrito = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=200, blank=True)    
    prefijo = models.CharField(default = 57, max_length=200, blank=True)
    telefono = models.CharField(max_length=50, blank=True, verbose_name='telefono (Movil)')
    fijo = models.CharField(max_length=50, blank=True, verbose_name='telefono (Fijo)')    
    email = models.EmailField(max_length=50, blank=True, verbose_name='Correo electrónico')
    estatus = models.CharField(max_length=12,  blank=True, default=1, choices=(('1', 'Activo'), ('0', 'Retirado'),))
    epsactual = models.CharField(max_length=50, blank=True, verbose_name='Eps donde se Encuentra Actualmente') 
    epstraslado = models.CharField(max_length=50, blank=True, verbose_name='Eps a donde quiere ser Trasladado') 
    pinseguridadsocial = models.CharField(max_length=15, blank=True, verbose_name='PIN con que ingresa Seguridad Social') 
    
    def servicios_afiliado(self):
        return "/".join([str(p) for p in self.servicios.all()]) 

    class Meta:
        #ordering = ["nombre"]
        verbose_name_plural = "Afiliados"
       
    def __str__(self):
        cadena = "{0} {1}: Celular: ({2})-{3} - CC: {4} - {5}  "
        return cadena.format(self.nombre, self.apellido, self.prefijo, self.telefono, self.documento, self.rango)      

    def pago_recientemente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.fecha_pago <= now
    pago_recientemente.admin_order_field = 'fecha_pago'
    pago_recientemente.boolean = True
    pago_recientemente.short_description = 'Pago recently?'




class EmpresaAfiliada(models.Model):
    nombre = models.CharField(max_length=50)
    nit = models.CharField(max_length=50, blank = True, unique=True)
    prefijo = models.CharField(default = 57, max_length=2, blank=False)
    telefono = models.CharField(max_length=50, blank=True, verbose_name='Telefono de la Empresa')    
    def __str__(self):
        cadena = "{0} {1}"
        return cadena.format(self.nombre, self.nit, self.telefono)  
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Empresas Afiliadas"       

class Empleado(models.Model):
    empresaafiliada = models.ForeignKey(EmpresaAfiliada, on_delete=models.CASCADE,verbose_name='Quién realizó el Pago?')  
    nombre = models.CharField(max_length=50)
    tipoDoc = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, verbose_name='Tipo de Documento')      
    documento = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50, blank=True, verbose_name='telefono (Movil)')

    def __str__(self):
        cadena = "{0} {1} {2} {3} "
        return cadena.format(self.nombre, self.tipoDoc, self.documento, self.telefono) 

class Pago(models.Model):
    afiliado = models.ForeignKey(Afiliado, on_delete=models.CASCADE,verbose_name='Quién realizó el Pago?')    
    fecha_pago = models.DateField(null=True, blank=True) 
    monto = models.FloatField(blank=True, null = True)
    recibo = models.IntegerField(blank=True, null = True)
    observacion = models.CharField(max_length=50, blank=True, verbose_name='Concepto de pago' )
    
    def __str__(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.afiliado, self.fecha_pago, self.monto)

class Planilla(models.Model):
    afiliado = models.ForeignKey(Afiliado, on_delete=models.CASCADE,verbose_name='A quien se la paga la planilla?') 
    año = models.ForeignKey(Año, on_delete=models.CASCADE, verbose_name='Año')    
    mes1 = models.CharField(max_length=12, blank=True, verbose_name='mes 1' )
    mes2 = models.CharField(max_length=12, blank=True, verbose_name='mes 2' )
    numero = models.CharField(max_length=5, blank=True, verbose_name='Numero Planilla' )
    monto = models.FloatField(blank=True, null = True)
    
    def __str__(self):
        cadena = "{0} {1} {2} {3}"
        return cadena.format(self.mes1, self.mes2, self.numero, self.monto)        

     

class PagoEmpresa(models.Model):
    empresaafiliada = models.ForeignKey(EmpresaAfiliada, on_delete=models.CASCADE,verbose_name='Quién realizó el Pago?')    
    fecha_pago = models.DateField(null=True, blank=True) 
    monto = models.FloatField(blank=True, null = True)
    recibo = models.IntegerField(blank=True, null = True)
    observacion = models.CharField(max_length=50, blank=True, verbose_name='Concepto de pago' )
    foto = models.ImageField(upload_to = 'Consignaciones/', default = 'Foto recibo de Pago')

    
    def __str__(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.afiliado, self.fecha_pago, self.monto)         

class Familia(models.Model): 
    vinculo = models.ForeignKey(Vinculo, on_delete=models.CASCADE) 
    afiliado = models.ForeignKey(Afiliado, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=50, blank=True)
    tipoDoc = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, verbose_name='Tipo de Documento') 
    documento = models.CharField(max_length=50, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True) 
    
    def __str__(self):
        cadena = "{0} {1}"
        return cadena.format(self.nombre_completo)          
        
