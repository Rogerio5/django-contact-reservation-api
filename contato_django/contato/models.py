from django.db import models


class Mensagem(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)  # data de criação automática

    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.nome} - {self.email}"


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    pet_nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    data = models.DateField()
    observacoes = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)  # útil para histórico/admin
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="reservas",
        null=True,   # permite valores nulos para facilitar migração inicial
        blank=True   # permite deixar em branco no admin/forms
    )

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-data"]

    def __str__(self):
        return f"{self.pet_nome} - {self.data} ({self.categoria if self.categoria else 'Sem categoria'})"
