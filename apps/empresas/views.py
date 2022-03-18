from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa
# Create your views here.


class CreateCompany(CreateView):
    model = Empresa
    fields = ['name']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.company = obj
        funcionario.save()
        return HttpResponse('ok')


class EditCompany(UpdateView):
    model = Empresa
    fields = ['name']
