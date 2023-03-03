from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def pagina_inicio(request, nombre):
    contexto = {
        "nombre":nombre,
        "guess":"Sofia"
    }
    return render(request, "plantilla1.html", context= contexto)

def hora(request):
    contexto = {
        "fecha" : datetime.now()
    }
    return render(request, "inicio.html", context=contexto)
