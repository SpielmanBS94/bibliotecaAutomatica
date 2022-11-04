from django.contrib import admin
from app.models.Lector import Lector
from app.models.Libro import Libro
# Register your models here.

class LectorAdmin(admin.ModelAdmin):
    list_display=("numSocio","nombre","rut","apellido","direccion")
    
class LibroAdmin(admin.ModelAdmin):
    list_display=("nombre","tipo","editorial","anio")
    
admin.site.register(Lector,LectorAdmin)
admin.site.register(Libro,LibroAdmin)