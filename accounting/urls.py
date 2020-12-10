"""Accounting URLs modulo"""

# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework import routers

# Views
from accounting.views.cobranzas import (
    CobranzaViewSet, CobranzaListView, CobranzaAgregarTemplateView,
    CobranzaDetalleView, CobranzaEditarTemplateView, CobranzaEliminarView
)

router = routers.DefaultRouter()
router.register(r'cobranza', CobranzaViewSet)

urlpatterns = [
    # API
    path(r'api/', include(router.urls)),

    # Cobranza cliente
    path('cobranza/', CobranzaListView.as_view(), name='cobranza-listado'),
    path('cobranza/agregar', CobranzaAgregarTemplateView.as_view(), name='cobranza-agregar'),
    path('cobranza/<int:pk>/', CobranzaDetalleView.as_view(), name='cobranza-detalle'),
    path('cobranza/<int:pk>/editar/', CobranzaEditarTemplateView.as_view(), name='cobranza-modificar'),
    path('cobranza/<int:pk>/eliminar/', CobranzaEliminarView.as_view(), name='cobranza-eliminar'),
]