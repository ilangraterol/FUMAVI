from django.db import models

# Create your models here.
class Notificaciones(models.Model):
	tipo = models.CharField(max_length=12, choices=(('Cobro', 'Cobro'), ('Promocion', 'Promocion'),('Empresas', 'Empresas')))
	saludo = models.CharField(max_length=250, blank=True)
	asunto = models.CharField(max_length=250, blank=True)
	asunto2 = models.CharField(max_length=250, blank=True)
	mensaje = models.TextField(max_length=250, blank=True)
	despedida = models.CharField(max_length=250, blank=True)

	def __str__(self):
    		cadena = "({0}) {1}"
    		return cadena.format(self.tipo, self.asunto)    

	class Meta:
        #ordering = ["nombre"]
        	verbose_name_plural = "Configuracion Mensajes Whatsapp"  	
