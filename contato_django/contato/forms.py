from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["pet_nome", "telefone", "data", "observacoes"]
        widgets = {
            "observacoes": forms.Textarea(attrs={"rows": 4, "class": "form-control", "placeholder": "Alguma observação?"}),
            "data": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "pet_nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o nome do pet"}),
            "telefone": forms.TextInput(attrs={"class": "form-control", "placeholder": "(xx) xxxxx-xxxx"}),
        }

    def clean_data(self):
        data = self.cleaned_data.get("data")
        if data:
            reservas_no_dia = Reserva.objects.filter(data=data).count()
            if reservas_no_dia >= 4:
                raise forms.ValidationError(
                    "Não é possível agendar mais de 4 reservas para este dia."
                )
        return data
