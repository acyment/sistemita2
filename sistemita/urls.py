from django.urls import path, include
from rest_framework import routers

from core.views import HomeView, ClienteDetalleView, ClienteModificarView, ClienteAgregarView, ClienteListView, \
    UsuarioListView, ClienteEliminarView, DistritoViewSet, LocalidadViewSet, ProveedorListView, ProveedorDetalleView, \
    ProveedorAgregarView, ProveedorModificarView, ProveedorEliminarView

router = routers.DefaultRouter()
router.register(r'distrito', DistritoViewSet)
router.register(r'localidad', LocalidadViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('facturacion_clientes.urls'))
    path('accounts/', include('django.contrib.auth.urls')),
    path('', HomeView.as_view(), name='home'),

    path(r'api/', include(router.urls)),

    path('cliente/', ClienteListView.as_view(), name='cliente-listado'),
    path('cliente/<int:pk>/', ClienteDetalleView.as_view(), name='cliente-detalle'),
    path('cliente/<int:pk>/editar/', ClienteModificarView.as_view(), name='cliente-modificar'),
    path('cliente/<int:pk>/eliminar/', ClienteEliminarView.as_view(), name='cliente-eliminar'),
    path('cliente/agregar/', ClienteAgregarView.as_view(), name='cliente-agregar'),

    path('proveedor/', ProveedorListView.as_view(), name='proveedor-listado'),
    path('proveedor/<int:pk>/', ProveedorDetalleView.as_view(), name='proveedor-detalle'),
    path('proveedor/<int:pk>/editar/', ProveedorModificarView.as_view(), name='proveedor-modificar'),
    path('proveedor/<int:pk>/eliminar/', ProveedorEliminarView.as_view(), name='proveedor-eliminar'),
    path('proveedor/agregar/', ProveedorAgregarView.as_view(), name='proveedor-agregar'),

    path('usuarios/', UsuarioListView.as_view(), name='usuario-list')
]
