from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# -------------------------------
# Rotas da API (com Router DRF)
# -------------------------------
router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet, basename='categoria')

urlpatterns = [
    # -------------------------------
    # Rotas HTML (templates)
    # -------------------------------
    path('', views.home, name='home'),
    path('contato/', views.contato_view, name='contato'),
    path('reserva/', views.reserva_view, name='reserva'),

    # -------------------------------
    # Rotas API - Contatos
    # -------------------------------
    path('api/contatos/', views.ContatoListCreate.as_view(), name='api-contatos'),
    path('api/contatos/<int:pk>/', views.ContatoRetrieveUpdateDestroy.as_view(), name='api-contato-detalhe'),

    # -------------------------------
    # Rotas API - Reservas
    # -------------------------------
    path('api/reservas/', views.ReservaListCreate.as_view(), name='api-reservas'),
    path('api/reservas/<int:pk>/', views.ReservaRetrieveUpdateDestroy.as_view(), name='api-reserva-detalhe'),

    # -------------------------------
    # Rotas API - Categorias (via Router)
    # -------------------------------
    path('api/', include(router.urls)),
]
