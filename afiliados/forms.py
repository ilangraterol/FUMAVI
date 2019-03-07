from django import forms
from .models import  Afiliado, Pago, EmpresaAfiliada




class RegistroAfiliado(forms.ModelForm):

    class Meta:
        model = Afiliado
        fields = [ 
            'fecha_afiliacion' ,          
            'nombre',
            'apellido',
            'sexo',
            'tipoDoc',
            'documento', 
            'fecha_nacimiento',            
            'rango',
            'servicios',
            'distrito',
            'direccion',
            'ciudad',                       
            'departamento',
            'prefijo',
            'mensualidad',
            'telefono',
            'email',
            'estatus',
            

        ]
        labels = {     

            'nombre':'Nombre del Afiliado',
            'apellido':'Apellidos',
            'sexo:' : 'Sexo', 
            'tipoDoc' : 'Tipo de Documento',            
            'documento':'Numero de Documento',
            'rango':'Rango',
            'servicios':'Servicios',
            'distrito':'Distrito',
            'ciudad':'Ciudad',                     
            'direccion':'Direccion',
            'departamento':'Departamento',
            'prefijo':'Prefijo',            
            'telefono':'Telefono',
            'email':'Correo Electronico',
            'estatus':'Estatus',
          
        }
        widgets = {     
        
          #  'fecha_afiliacion': forms.SelectDateWidget(attrs={'class':'form-control'}),

            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-control'}),           
            'rango': forms.Select(attrs={'class':'form-control'}),
            'distrito': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.Select(attrs={'class':'form-control'}),
            'departamento': forms.Select(attrs={'class':'form-control'}),
            'tipoDoc': forms.Select(attrs={'class':'form-control'}),
            'documento': forms.TextInput(attrs={'class':'form-control'}),
            'prefijo': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'estatus': forms.Select(attrs={'class':'form-control'}),
         

        }

class RegistroEmpresa(forms.ModelForm):

    class Meta:
        model = EmpresaAfiliada
        fields = [                 
            'nombre',
            'nit',
            'telefono',
                   
        ]
        labels = {     

            'nombre':'Nombre de la Empresa',
            'nit':'nit',
            'telefono:' : 'telefono',            
          
        }
        widgets = {     
        
          #  'fecha_afiliacion': forms.SelectDateWidget(attrs={'class':'form-control'}),

            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'nit': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),           
       
            
        }        

class RegistroPago(forms.ModelForm):

    class Meta:
        model = Pago
        fields = [ 
            'afiliado' ,          
            'fecha_pago',
            'monto',
            'recibo',
            'observacion',          
            
            

        ]
        labels = {     

            'afiliado':'Nombre del Afiliado',
            'fecha_pago':'Fecha de Pago',
            'monto:' : 'Monto',                         
            'recibo':'N° Recibo',
            'observacion':'Observacion',
            
          
        }
        widgets = {     
        
          #  'fecha_afiliacion': forms.SelectDateWidget(attrs={'class':'form-control'}),

            'afiliado': forms.Select(attrs={'class':'form-control'}),
            'fecha_pago': forms.TextInput(attrs={'class':'form-control'}),
            'monto': forms.TextInput(attrs={'class':'form-control'}),           
            'recibo': forms.TextInput(attrs={'class':'form-control'}),
            'observacion': forms.TextInput(attrs={'class':'form-control'}),            

        }        

