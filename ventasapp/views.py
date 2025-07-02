
import traceback
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.utils import timezone

from django.http import  JsonResponse
from  django.views.decorators.csrf import csrf_exempt
import json
from decimal import Decimal
from datetime import date

from ventasapp.models import Categoria
from ventasapp.models import Cliente
from ventasapp.models import Unidades
from ventasapp.models import Productos
from ventasapp.models import cabeceraVentas,Tipo,Parametros,detalleVentas

from django.db.models import Q
from .forms import CategoriaForm
from .forms import ClienteForm
from .forms import UnidadForm
from .forms import ProductoForm
from .forms import VentaForm
from .forms import DetalleVentaForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from django.template.loader import get_template
from django.http import HttpResponse
from weasyprint import HTML
from io import BytesIO

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
    ventas = cabeceraVentas.objects.filter(estado=True)
    if queryset:
        ventas = ventas.filter(
            Q(total__icontains=queryset) | Q(nrodoc__icontains=queryset) | Q(tipo_id_id__descripcion__icontains=queryset) |
            Q(cliente_id__nombres__icontains=queryset) | Q(cliente_id__apellidos__icontains=queryset), estado=True
        ).distinct()
    context = {
        'ventas': ventas
    }
    return render(request, "movimiento/registro-ventas/listarventas.html", context)

@login_required
def crearventa(request):
    if request.method == 'POST':
        try:
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({'success': False, 'message': "Error: El cuerpo de la petición no es JSON válido."}, status=400)

            form = VentaForm(data)
            detalles_data = data.get('detalles', [])

            if form.is_valid():
                with transaction.atomic():
                    cliente_obj = form.cleaned_data['cliente']
                    tipo_obj = form.cleaned_data['tipo']
                    fecha_venta = form.cleaned_data['fecha_venta']
                    nrodoc = Parametros.actualizar_numeracion(tipo_obj.pk)
                    cabecera_venta = cabeceraVentas.objects.create(
                        cliente_id=cliente_obj,
                        tipo_id=tipo_obj,
                        fecha_venta=fecha_venta,
                        nrodoc=nrodoc,
                        total=Decimal('0.00'), 
                        subtotal=Decimal('0.00'),
                        igv=Decimal('0.00'),
                        estado=True,
                    )

                    if not detalles_data: 
                        pass 

                    total_venta_calculado = Decimal('0.00')
                    subtotal_venta_calculado = Decimal('0.00')
                    igv_venta_calculado = Decimal('0.00') 

                    for item_data in detalles_data:
                        detalle_form = DetalleVentaForm(item_data)
                        if detalle_form.is_valid():
                            producto_id = detalle_form.cleaned_data['producto_id']
                            precio_detalle = detalle_form.cleaned_data['precio']
                            cantidad_detalle = detalle_form.cleaned_data['cantidad']
                            importe_detalle = detalle_form.cleaned_data['importe'] 

                            producto = Productos.objects.get(pk=producto_id)

                            if producto.cantidad < cantidad_detalle:
                                transaction.set_rollback(True) 
                                return JsonResponse({'success': False, 'message': f"Stock insuficiente para {producto.descripcion}. Disponible: {producto.cantidad}, Solicitado: {cantidad_detalle}"}, status=400)

                            detalleVentas.objects.create(
                                venta_id=cabecera_venta,
                                producto_id=producto,
                                precio=precio_detalle,
                                cantidad=cantidad_detalle,
                                importe=importe_detalle
                            )

                            Productos.actualizar_stock(producto.pk, cantidad_detalle)
                            

                            subtotal_venta_calculado += importe_detalle
                            
                        else:
                            transaction.set_rollback(True) 
                            error_detalle_msg = ", ".join([f"{k}: {v[0]}" for k, v in detalle_form.errors.items()])
                            return JsonResponse({'success': False, 'message': f"Error en el detalle del producto (ID {item_data.get('producto_id', 'N/A')}): {error_detalle_msg}"}, status=400)
                    
                    igv_venta_calculado = subtotal_venta_calculado * Decimal('0.18')
                    total_venta_calculado = subtotal_venta_calculado + igv_venta_calculado

                    cabecera_venta.subtotal = subtotal_venta_calculado
                    cabecera_venta.igv = igv_venta_calculado
                    cabecera_venta.total = total_venta_calculado
                    cabecera_venta.save() 

                messages.success(request, f"Venta {nrodoc} registrada correctamente.")
                return JsonResponse({'success': True, 'message': f"Venta {nrodoc} registrada correctamente."})

            else: 
                errors = form.errors.as_json()
                return JsonResponse({'success': False, 'message': 'Por favor, corrija los errores en el formulario de la venta.', 'errors': json.loads(errors)}, status=400)

        except Productos.DoesNotExist:
            transaction.set_rollback(True)
            return JsonResponse({'success': False, 'message': "Error: Uno de los productos seleccionados no existe."}, status=400)
        except ValueError as ve:
            transaction.set_rollback(True)
            return JsonResponse({'success': False, 'message': str(ve)}, status=400)
        except Exception as e:
            print("\n--- ERROR INESPERADO EN VISTA crearventa ---")
            print(f"Tipo de error: {type(e)}")
            print(f"Mensaje de error: {e}")
            traceback.print_exc()
            print("--- FIN ERROR INESPERADO EN VISTA crearventa ---\n")
            transaction.set_rollback(True) 
            return JsonResponse({'success': False, 'message': "Ocurrió un error inesperado al guardar la venta."}, status=500)
    else:
        form = VentaForm()
        context = {
            'form': form,
            'fecha_actual': date.today().strftime('%d/%m/%Y'),
        }
        return render(request, "movimiento/registro-ventas/crearventas.html", context)

@login_required
@require_POST 
def eliminarventa(request, pk):
    try:
        venta = get_object_or_404(cabeceraVentas, pk=pk)
        
        with transaction.atomic():
            
            for detalle in venta.detalles.all(): 
                producto = detalle.producto_id
                producto.cantidad += detalle.cantidad 
                producto.save()

            venta.delete() 

        return JsonResponse({'success': True, 'message': f"Venta {venta.nrodoc} eliminada correctamente."})
    except Exception as e:
        print(f"Error al eliminar venta {pk}: {e}")
        return JsonResponse({'success': False, 'message': f'Error al eliminar la venta: {e}'}, status=500)

@login_required
def obtener_datos_producto(request):
    """
    Retorna los datos de un producto (precio, stock, unidad) dado su ID.
    """
    producto_id = request.GET.get('producto_id')
    if not producto_id:
        return JsonResponse({'error': 'ID de producto no proporcionado'}, status = 400)
    
    try:
        producto =Productos.objects.get(pk=producto_id)
        data ={
            'precio': str(producto.precio),
            'stock' : producto.cantidad,
            'unidad_descripcion': producto.unidad.descripcion if producto.unidad else '',
        }
        return JsonResponse(data)
    except Productos.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'Error interno: {str(e)}'}, status = 500)

@login_required
def obtener_datos_cliente(request):
    """
    Retorna los datos del cliente (ruc_dni, direccion) dado su ID.
    """
    cliente_id = request.GET.get('cliente_id')
    if not cliente_id:
        return JsonResponse({'error': 'ID de cliente no proporcionado'}, status = 400)
    
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
        data = {
            'ruc_dni' : cliente.ruc_dni if cliente.ruc_dni else '',
            'direccion' : cliente.direccion if cliente.direccion else '',
            'nombres_completos' : f"{cliente.nombres} {cliente.apellidos}"
        }

        return JsonResponse(data)
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado'}, status = 404)
    except Exception as e:
        return JsonResponse({'error' : f'Error interno: {str(e)}'}, status = 500)
    

@login_required
def obtener_datos_tipo_documento(request):
    """
    Retorna la serie y numeración del documento dado un tipo de documento ID.
    """
    tipo_id = request.GET.get('tipo_id')
    if not tipo_id:
        return JsonResponse({'error' : 'ID de tipo de documento no proporcionado'}, status = 400)
    
    try:
        parametro = Parametros.objects.filter(tipo_id=tipo_id).first()
        if not parametro:
            return JsonResponse({'error': 'Parametro de tipo de documento no encontrado'}, status=404)
        
        data = {
            'serie' : parametro.serie,
            'numeracion' : parametro.numeracion,
        }
        return JsonResponse(data)
    except Parametros.DoesNotExist:
        return JsonResponse({'error' : 'Parametro de tipo de documento no encontrado'}, status = 404)
    except Exception as e:
        return JsonResponse({'error': f'Error interno: {str(e)}'}, status = 500)

@login_required
def verdetalleventa(request,pk):
    venta = cabeceraVentas.objects.get(pk=pk)
    context = {
        'detalle': venta,
    }
    return render(request, "movimiento/registro-ventas/detalleventa.html", context)

@login_required
def generarpdf(request, pk):
    venta = cabeceraVentas.objects.get(pk=pk)
    template = get_template('movimiento/registro-ventas/detallepdf.html')  # Ruta correcta de la plantilla
    context = {
        'detalle': venta,
        'ahora': timezone.localtime(),
    }
    html = template.render(context)  # Renderiza la plantilla con el contexto
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="venta_{venta.nrodoc}.pdf"'
    HTML(string=html).write_pdf(response)  # Genera el PDF con WeasyPrint
    return response