from django.forms import ModelForm
from appcrud.models import Reservas


# Create the form class.
class ReservasForm(ModelForm):
    class Meta:
        model = Reservas
        fields = ['Req_nome', 'Mat_nro', 'Curso_nome', 'Sala_nro', 'Data', 'Horario', ]
