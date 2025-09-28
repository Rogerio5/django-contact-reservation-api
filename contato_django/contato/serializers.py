from rest_framework import serializers
from .models import Mensagem, Reserva, Categoria


class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = ["id", "nome", "email", "mensagem", "criado_em"]


class CategoriaSerializer(serializers.ModelSerializer):
    # Exibe as reservas ligadas a essa categoria (somente leitura)
    reservas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Categoria
        fields = ["id", "nome", "reservas"]


class ReservaSerializer(serializers.ModelSerializer):
    # Mostra o nome da categoria junto com o ID
    categoria_nome = serializers.CharField(source="categoria.nome", read_only=True)

    class Meta:
        model = Reserva
        fields = [
            "id",
            "pet_nome",
            "telefone",
            "data",
            "observacoes",
            "criado_em",
            "categoria",       # ID da categoria
            "categoria_nome",  # Nome da categoria (somente leitura)
        ]

    def validate(self, data):
        """
        Regra de negócio: máximo de 4 reservas por dia.
        """
        data_reserva = data.get("data")
        if data_reserva and Reserva.objects.filter(data=data_reserva).count() >= 4:
            raise serializers.ValidationError(
                "Não é possível agendar mais de 4 reservas para este dia."
            )
        return data
