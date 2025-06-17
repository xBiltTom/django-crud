from django.urls import path,include
from ventasapp.views import listarcategoria,agregarcategoria,editarcategoria,eliminarcategoria
from ventasapp.views import listarcliente, agregarcliente, editarcliente, eliminarcliente
from ventasapp.views import listarunidades,agregarunidades,editarunidad,eliminarunidad
from django.contrib.auth import views

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
