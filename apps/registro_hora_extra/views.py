from django.shortcuts import render
from .models import RegistroHoraExtra
from django.views.generic import CreateView, ListView
# Create your views here.

class CreateOvertime(CreateView):
    pass

class ListOvertime(ListView):
    models = RegistroHoraExtra
    template_name='overtime/overtime.html'
    def get_queryset(self):
        log_company = self.request.user.funcionario.company
        return RegistroHoraExtra.objects.filter(worker__company=log_company)
    