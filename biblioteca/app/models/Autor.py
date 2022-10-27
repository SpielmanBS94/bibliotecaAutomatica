from django.db import models
from django.forms import ModelForm
from .Libro import Libro

class Autor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=10)
    nacionalidad = models.CharField(max_length=10)
    fechaNacimiento = models.DateField()
    libros = models.ManyToManyField(Libro)
class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        exclude = []