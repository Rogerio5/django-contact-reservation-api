from django.contrib import admin
from .models import Mensagem, Reserva


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "criado_em")  # agora funciona
    search_fields = ("nome", "email")
    list_filter = ("criado_em",)  # filtro lateral por data de criação


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("pet_nome", "telefone", "data", "criado_em")
    search_fields = ("pet_nome", "telefone")
    list_filter = ("data", "criado_em")
