from django.db import models
from django.forms import ModelForm
from .Lector import Lector
from .Prestamo import Prestamo

class Multa(models.Model):
    prestamo = models.OneToOneField(Prestamo,on_delete=models.CASCADE,primary_key=True,)
    fechaInicio = models.DateField()
    fechaFin = models.DateField(null=True,blank=True)
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)

    def calcularFechaFin(self):
        pass
class MultaForm(ModelForm):
    class Meta:
        model = Multa
        fields = '__all__'
        exclude = ['fechaFin']