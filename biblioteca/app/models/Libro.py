from django.db import models
from django.forms import ModelForm

class Libro(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipos = [('00', 'Sin Tipo Asignado'),
            ('01', 'Epico'),
            ('02', 'Terror'),
            ('03', 'Novela'),
            ('04', 'Revista'),
            ('05', 'Ficcion')]
    tipo = models.CharField(max_length=2,choices=tipos,default='00')
    editoriales = [('00', 'Generica'),
            ('01', 'Santillana'),
            ('02', 'ZigZag'),
            ('03', 'ContraPunto'),
            ('04', 'Antartica'),
            ('05', 'UTFSM')]
    editorial = models.CharField(max_length=2,choices=editoriales,default='00')
    anio = models.DateField()
class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        exclude = []