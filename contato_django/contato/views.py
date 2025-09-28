from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Mensagem, Reserva, Categoria
from .forms import ReservaForm

# -------------------------------
# Views tradicionais (HTML)
# -------------------------------

def home(request):
    return render(request, "home.html")


def contato_view(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        mensagem = request.POST.get("mensagem")

        if nome and email and mensagem:
            Mensagem.objects.create(
                nome=nome,
                email=email,
                mensagem=mensagem
            )
            return render(request, "contato.html", {"sucesso": True})

    return render(request, "contato.html")


def reserva_view(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Reserva efetuada com sucesso!")
            return redirect("reserva")
    else:
        form = ReservaForm()

    return render(request, "reserva.html", {"form": form})


# -------------------------------
# Views da API (DRF)
# -------------------------------

from rest_framework import generics, filters, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MensagemSerializer, ReservaSerializer, CategoriaSerializer


# -------------------------------
# Contatos (Mensagens)
# -------------------------------

class ContatoListCreate(generics.ListCreateAPIView):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome', 'email']          # permite buscar por nome ou email
    ordering_fields = ['criado_em']            # permite ordenar por data de criação


class ContatoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer


# -------------------------------
# Reservas
# -------------------------------

class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['data', 'categoria']   # permite filtrar por data ou categoria
    search_fields = ['pet_nome', 'telefone']   # permite buscar por nome do pet ou telefone
    ordering_fields = ['data', 'criado_em']    # permite ordenar por data ou criado_em


class ReservaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


# -------------------------------
# Categorias
# -------------------------------

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    # Endpoint extra: /api/categorias/<id>/reservas/
    @action(detail=True, methods=["get"])
    def reservas(self, request, pk=None):
        categoria = self.get_object()
        reservas = categoria.reservas.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)
