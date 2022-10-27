from django.db import models
from django.forms import ModelForm
from .Libro import Libro
class Copia(models.Model):
    id = models.BigAutoField(primary_key=True)
    estados = [('00', 'Disponible'),
            ('01', 'Prestado'),
            ('02', 'No Disponible')]
    tipo = models.CharField(max_length=2,choices=estados,default='00')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    def devolver(self):
        pass
    def prestar(self):
        pass
class CopiaForm(ModelForm):
    class Meta:
        model = Copia
        fields = '__all__'
        exclude = []