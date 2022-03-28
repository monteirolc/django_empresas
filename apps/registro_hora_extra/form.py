from django.forms import ModelForm
from .models import RegistroHoraExtra
from apps.funcionarios.models import Funcionario


class OvertimeForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(OvertimeForm, self).__init__(*args,**kwargs)
        self.fields['worker'].queryset = Funcionario.objects.filter(company = user.funcionario.company)

    class Meta:
        model = RegistroHoraExtra
        fields = ['reason', 'worker', 'hours']