from django.db import models
from django.forms import ModelForm
from django.forms import PasswordInput

class Lector(models.Model):
    numSocio = models.CharField(primary_key=True,max_length=15)
    nombre = models.CharField(max_length=25)
    rut = models.CharField(max_length = 10)
    apellido = models.CharField(max_length=25)
    direccion = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    
    def comprobarMultasPendientes(self):
        pass
    
class LectorForm(ModelForm):
    class Meta:
        model = Lector
        fields = ['rut','nombre','apellido','direccion','password']
        widgets = {
        'password': PasswordInput(),
        }
        exclude = ['numSocio']