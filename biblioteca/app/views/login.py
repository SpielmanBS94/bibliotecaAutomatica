from django.shortcuts import render
from app.models.Lector import Lector
from app.models.Libro import Libro
from django.core.exceptions import ObjectDoesNotExist
import datetime
# Create your views here.
def logIn(request):
    try:
        usuario = Lector.objects.get(numSocio=request.POST["user"],password=request.POST["pass"])
    except ObjectDoesNotExist:
        return render(request, "home.html", {"error":True,"mensaje":"Revise los datos"},status=404)
    return render(request, "login.html", {},status=200)

def resultados(request):
    libros = Libro.objects.filter(tipo=request.POST["opcion"])
    return render(request,"resultados.html",{"libros":libros},status=200)
