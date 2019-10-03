from django.db import models




class Espe(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name='Nombre de la Especialidad')
    precio1 = models.FloatField(blank=True, null = True)
       
    def __str__(self):
        cadena = "{0} "
        return cadena.format(self.nombre) 
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Especialidades"      

class CentroMedico(models.Model):
    nombre = models.CharField(max_length=50, unique=True) 
    telefonos1 = models.CharField(max_length=50, blank=True, verbose_name='telefono (Fijo)')
    telefonos2 = models.CharField(max_length=50, blank=True, verbose_name='telefono (Opcional)') 
    direccion = models.CharField(max_length=200, blank=True)
    horario = models.CharField(max_length=70, blank=True, verbose_name='Horario de Atencion') 
    
    def __str__(self):
        cadena = "{0} "
        return cadena.format(self.nombre)  

class Contrato(models.Model):  
	
	fechainicio = models.DateField(null=True, blank=True, verbose_name='Fecha Inicio Convenio') 
	fechavencimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de Vencimiento')   
	centromedico = models.ForeignKey(CentroMedico, null = False, on_delete=models.CASCADE, verbose_name='Centro Medico o Doctor') 
	estatus = models.CharField(max_length=12, blank=True, choices=(('A', 'Activo'), ('P', 'Pendiente'),('R', 'Retirado'))) 
	observacion =  models.CharField(max_length=200, blank=True) 

class Especialidad(models.Model):
    nombre = models.ForeignKey(Espe, on_delete=models.CASCADE,verbose_name='Especialidad') 
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE,verbose_name='Contrato')    
    def __str__(self):
        cadena = "{0} "
        return cadena.format(self.nombre)   

class Asesor(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    cargo = models.CharField(max_length=50, unique=True)
    correo = models.CharField(max_length=50, blank = True, null	= True)
    telefonos1 = models.CharField(max_length=50, blank=True, verbose_name='Telefono')   
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE,verbose_name='Contrato') 
    def __str__(self):
        cadena = "{0} "
        return cadena.format(self.nombre)  

class Procedimiento (models.Model):
	nombre = models.CharField(max_length=50, unique=True, verbose_name='Nombre del procedimiento')
	precio1 = models.FloatField(blank=True, null = True, verbose_name='Precio Fumavi')
	precio2 = models.FloatField(blank=True, null = True, verbose_name='Precio Particular')
	precio3 = models.FloatField(blank=True, null = True, verbose_name='Monto a Consignar')
	contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE,verbose_name='Contrato') 
	def __str__(self):
		cadena = "{0}"
		return cadena.format(self.nombre)               






