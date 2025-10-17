from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/<int:categoria_id>/', views.categoria_view, name='categoria'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle'),
    path('buscar/', views.buscar, name='buscar'), # Nueva URL para la búsqueda
]