from django.shortcuts import render
from .models import Clientes

# Create your views here.

def index_vista(request):
        ListadoClientes=Clientes.objects.all()
        return render(request, "gestionarClientes.html",{"misclientes":ListadoClientes}) 