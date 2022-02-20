from django.forms import ModelForm
from appWeb.models import Reservas


class ReservasForm(ModelForm):
    class Meta:
        model = Reservas
        fields = ['Req_nome', 'Mat_nro', 'Curso_nome', 'Sala_nro', 'Data', 'Horario', ]
