from django.shortcuts import render,redirect
from ventasapp.models import Categoria
from ventasapp.models import Cliente
from django.db.models import Q
from .forms import CategoriaForm
from .forms import ClienteForm

# Create your views here.
def listarcategoria(request):
    queryset = request.GET.get("buscar")
    categoria = Categoria.objects.filter(estado=True)
    if queryset:
        categoria = categoria.filter(
            Q(descripcion__icontains=queryset),estado=True
        ).distinct()
    context = {
            'categoria':categoria}
    return render(request,"categoria/listar.html",context)

def agregarcategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarcategoria')
    else:
        form = CategoriaForm()
    context = {
        'form':form,
    }
    return render(request, "categoria/agregar.html", context)

def editarcategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listarcategoria')
    else:
        form = CategoriaForm(instance=categoria)
    context = {
        'form': form,
    }
    return render(request, "categoria/editar.html", context)

def eliminarcategoria(request, id):
    categoria= Categoria.objects.get(id=id)
    categoria.estado = False
    categoria.save()
    return redirect('listarcategoria')

def listarcliente(request):
    queryset = request.GET.get("buscar")
    cliente = Cliente.objects.filter(estado=True)
    if queryset:
        cliente = cliente.filter(
            Q(nombres__icontains=queryset) | Q(apellidos__icontains=queryset), estado=True
        ).distinct()
    context = {
            'cliente':cliente}
    return render(request,"cliente/listar.html",context)

def agregarcliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarcliente')
    else:
        form = ClienteForm()
    context = {
        'form':form,
    }
    return render(request, "cliente/agregar.html", context)

def editarcliente(request, id):
    cliente = Cliente.objects.get(idcliente=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listarcliente')
    else:
        form = ClienteForm(instance=cliente)
    context = {
        'form': form,
    }
    return render(request, "cliente/editar.html", context)

def eliminarcliente(request, id):
    cliente = Cliente.objects.get(idcliente=id)
    cliente.estado = False
    cliente.save()
    return redirect('listarcliente')



