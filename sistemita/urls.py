from django.urls import path, include
from rest_framework import routers

from core.views import \
    ClienteDetalleView, ClienteModificarView, ClienteAgregarView, ClienteListView, ClienteEliminarView, ClienteViewSet, \
    HomeView, UsuarioListView, DistritoViewSet, LocalidadViewSet, ProveedorListView, \
    ProveedorDetalleView, ProveedorAgregarView, ProveedorModificarView, ProveedorEliminarView, \
    FacturaModificarView, FacturaListView, FacturaEliminarView, FacturaDetalleView, FacturaAgregarView,\
    OrdenCompraListView, OrdenCompraDetalleView, OrdenCompraModificarView, OrdenCompraEliminarView, OrdenCompraAgregarView

router = routers.DefaultRouter()
router.register(r'distrito', DistritoViewSet)
router.register(r'localidad', LocalidadViewSet)
router.register(r'cliente', ClienteViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('facturacion_clientes.urls'))
    path('accounts/', include('django.contrib.auth.urls')),
    path('', HomeView.as_view(), name='home'),

    path(r'api/', include(router.urls)),

    path('factura/', FacturaListView.as_view(), name='factura-listado'),
    path('factura/<int:pk>/', FacturaDetalleView.as_view(), name='factura-detalle'),
    path('factura/<int:pk>/editar/', FacturaModificarView.as_view(), name='factura-modificar'),
    path('factura/<int:pk>/eliminar/', FacturaEliminarView.as_view(), name='factura-eliminar'),
    path('factura/agregar/', FacturaAgregarView.as_view(), name='factura-agregar'),

    path('ordencompra/', OrdenCompraListView.as_view(), name='ordencompra-listado'),
    path('ordencompra/<int:pk>/', OrdenCompraDetalleView.as_view(), name='ordencompra-detalle'),
    path('ordencompra/<int:pk>/editar/', OrdenCompraModificarView.as_view(), name='ordencompra-modificar'),
    path('ordencompra/<int:pk>/eliminar/', OrdenCompraEliminarView.as_view(), name='ordencompra-eliminar'),
    path('ordencompra/agregar/', OrdenCompraAgregarView.as_view(), name='ordencompra-agregar'),

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
