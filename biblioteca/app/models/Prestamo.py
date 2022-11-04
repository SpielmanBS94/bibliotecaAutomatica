from django.db import models
from django.forms import ModelForm
from .Lector import Lector
from .Copia import Copia

class Prestamo(models.Model):
    id = models.BigAutoField(primary_key=True)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    copias = models.ManyToManyField(Copia)
    
    def calcularFechaFin():
        pass
    def generarMulta():
        pass
    
class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'
        exclude = []