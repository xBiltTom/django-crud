from django.urls import path,include
from ventasapp.views import listarcategoria,agregarcategoria,editarcategoria,eliminarcategoria
from ventasapp.views import listarcliente, agregarcliente, editarcliente, eliminarcliente
from ventasapp.views import listarunidades,agregarunidades,editarunidad,eliminarunidad
from ventasapp.views import listarproductos,agregarproductos,editarproducto,eliminarproducto
from ventasapp.views import listarventas, crearventa, obtener_datos_cliente, obtener_datos_producto, obtener_datos_tipo_documento
from django.contrib.auth import views
from . import views
urlpatterns = [
    path('listarcategoria/', listarcategoria, name='listarcategoria'),
    path('agregarcategoria/', agregarcategoria, name='agregarcategoria'),
    path('editarcategoria/<int:id>/', editarcategoria, name='editarcategoria'),
    path('eliminarcategoria/<int:id>/', eliminarcategoria, name='eliminarcategoria'),
       
    ]

urlpatterns += [
    path('listarcliente/', listarcliente, name='listarcliente'),    
    path('agregarcliente/', agregarcliente, name='agregarcliente'),
    path('editarcliente/<int:id>/', editarcliente, name='editarcliente'),       
    path('eliminarcliente/<int:id>/', eliminarcliente, name='eliminarcliente'),
]

urlpatterns += [
    path('listarUnidades/',listarunidades, name='listarunidades'),
    path('agregarunidad/', agregarunidades, name='agregarunidad'),
    path('editarunidad/<int:id>/', editarunidad, name='editarunidad'),
    path('eliminarunidad/<int:id>/', eliminarunidad, name='eliminarunidad'),
]

urlpatterns += [
    path('listarproductos/',listarproductos, name='listarproductos'),
    path('agregarproducto/', agregarproductos, name='agregarproductos'),
    path('editarproducto/<int:id>/', editarproducto, name='editarproducto'),
    path('eliminarproducto/<int:id>/', eliminarproducto, name='eliminarproducto'),
]

urlpatterns += [
    path('',listarventas,name='listarventas'),
    path('crear', crearventa, name = 'crearventa'),
    path('eliminar/<int:pk>/', views.eliminarventa, name='eliminarventa'),
    path('api/obtener_datos_producto/', obtener_datos_producto, name = 'api_obtener_datos_producto'),
    path('api/obtener_datos_cliente/', obtener_datos_cliente, name = 'api_obtener_datos_cliente'),
    path('api/obtener_datos_tipo_documento/', obtener_datos_tipo_documento, name= 'api_obtener_datos_tipo_documento'),
    path('detalle/<int:pk>',views.verdetalleventa,name='detalleventa'),
    path('detalle/<int:pk>/pdf', views.generarpdf, name='generarpdf'),
]
