from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from ventasapp.models import Categoria
from ventasapp.models import Cliente
from ventasapp.models import Unidades
from ventasapp.models import Productos
from ventasapp.models import cabeceraVentas
from django.db.models import Q
from .forms import CategoriaForm
from .forms import ClienteForm
from .forms import UnidadForm
from .forms import ProductoForm
from django.contrib import messages

# Create your views here.
@login_required
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

@login_required
def agregarcategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría agregada correctamente")
            return redirect('categorias:listarcategoria')
    else:
        form = CategoriaForm()
    context = {
        'form':form,
    }
    return render(request, "categoria/agregar.html", context)

@login_required
def editarcategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría actualizada correctamente")
            return redirect('categorias:listarcategoria')
    else:
        form = CategoriaForm(instance=categoria)
    context = {
        'form': form,
    }
    return render(request, "categoria/editar.html", context)

@login_required
def eliminarcategoria(request, id):
    categoria= Categoria.objects.get(id=id)
    categoria.estado = False
    messages.success(request, "Categoría eliminada correctamente")
    categoria.save()
    return redirect('categorias:listarcategoria')

@login_required
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

@login_required
def agregarcliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente agregado correctamente")
            return redirect('clientes:listarcliente')
    else:
        form = ClienteForm()
    context = {
        'form':form,
    }
    return render(request, "cliente/agregar.html", context)

@login_required
def editarcliente(request, id):
    cliente = Cliente.objects.get(idcliente=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente actualizado correctamente")
            return redirect('clientes:listarcliente')
    else:
        form = ClienteForm(instance=cliente)
    context = {
        'form': form,
    }
    return render(request, "cliente/editar.html", context)

@login_required
def eliminarcliente(request, id):
    cliente = Cliente.objects.get(idcliente=id)
    cliente.estado = False
    messages.success(request, "Cliente eliminado correctamente")
    cliente.save()
    return redirect('clientes:listarcliente')

@login_required
def listarunidades(request):
    queryset = request.GET.get("buscar")
    unidad = Unidades.objects.filter(estado=True)
    if queryset:
        unidad = unidad.filter(
            Q(descripcion__icontains=queryset)
        ).distinct()
    context = {
            'unidades':unidad}
    return render(request,"unidades/listar.html",context)

@login_required
def agregarunidades(request):
    if request.method == 'POST':
        form = UnidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Unidad agregada correctamente")
            return redirect('unidades:listarunidades')
    else:
        form = UnidadForm()
    context = {
        'form':form,
    }
    return render(request, "unidades/agregar.html", context)

@login_required
def editarunidad(request, id):
    unidad = Unidades.objects.get(id=id)
    if request.method == 'POST':
        form = UnidadForm(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            messages.success(request, "Unidad actualizada correctamente")
            return redirect('unidades:listarunidades')
    else:
        form = UnidadForm(instance=unidad)
    context = {
        'form': form,
    }
    return render(request, "unidades/editar.html", context)

@login_required
def eliminarunidad(request, id):
    unidad = Unidades.objects.get(id=id)
    unidad.estado = False
    messages.success(request, "Unidad eliminada correctamente")
    unidad.save()
    return redirect('unidades:listarunidades')

@login_required
def listarproductos(request):
    queryset = request.GET.get("buscar")
    producto = Productos.objects.filter(estado=True)
    if queryset:
        producto = producto.filter(
            Q(descripcion__icontains=queryset),estado=True
        ).distinct()
    context = {
            'productos':producto}
    return render(request,"productos/listar.html",context)

@login_required
def agregarproductos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:listarproductos')
    else:
        form = ProductoForm()
    context = {
        'form':form,
    }
    return render(request, "productos/agregar.html", context)

@login_required
def editarproducto(request, id):
    producto = Productos.objects.get(id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado correctamente")
            return redirect('productos:listarproductos')
    else:
        form = ProductoForm(instance=producto)
    context = {
        'form': form,
    }
    return render(request, "productos/editar.html", context)

@login_required
def eliminarproducto(request, id):
    producto = Productos.objects.get(id=id)
    producto.estado = False
    producto.save()
    return redirect('productos:listarproductos')

@login_required
def listarventas(request):
    queryset = request.GET.get("buscar")
    venta = cabeceraVentas.objects.filter(estado=True)
    if queryset:
        venta = venta.filter(
            Q(total__icontains=queryset) | Q(nrodoc__icontains=queryset), estado=True
        ).distinct()
    context = {
            'ventas':venta}
    return render(request,"movimiento/registro-ventas/listarventas.html",context)

@login_required
def crearventa(request):
    pass