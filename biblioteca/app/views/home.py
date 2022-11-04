from django.shortcuts import render
from app.models.Lector import LectorForm
import datetime
# Create your views here.
def home(request):
    
    return render(request, "home.html", {},status=200)

def registrar(request):
    if request.method=="GET":
        form = LectorForm().as_table
        return render(request, "registrar.html", {"formulario":form},status=200)
    else:
        lector = LectorForm(request.POST)
        if lector.is_valid():
            today = datetime.date.today()
            year = today.strftime("%Y")
            dia = today.strftime("%d")
            lectorObj = lector.save(commit=False)
            lectorObj.numSocio = year+dia+str(int(year)*int(dia))
            lectorObj.save()
        form = LectorForm().as_table
        return render(request, "registrar.html", {"formulario":form,"lector":lectorObj},status=200)