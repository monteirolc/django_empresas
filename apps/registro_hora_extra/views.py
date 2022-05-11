from django.shortcuts import render
from .models import RegistroHoraExtra
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponse
import json
from .form import OvertimeForm
# Create your views here.

class CreateOvertime(CreateView):
    model = RegistroHoraExtra
    template_name = 'overtime/overtime_form.html'
    form_class = OvertimeForm

    def get_form_kwargs(self):
        kwargs = super(CreateOvertime, self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs

class ListOvertime(ListView):
    models = RegistroHoraExtra
    template_name='overtime/overtime.html'
    def get_queryset(self):
        log_company = self.request.user.funcionario.company
        return RegistroHoraExtra.objects.filter(worker__company=log_company)
        
class ChangeOvertime(UpdateView):
    model = RegistroHoraExtra
    template_name = 'overtime/overtime_form.html'
    form_class = OvertimeForm

    def get_form_kwargs(self):
        kwargs = super(ChangeOvertime, self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs

class DeleteOvertime(DeleteView):
    model = RegistroHoraExtra
    template_name = "overtime/overtime_delete.html"
    success_url = reverse_lazy('list_overtime')

class UsedOvertime(View):
    def post(self, *args, **kwargs):
        response = json.dumps({'mensagem': 'Requisição executada', 'hours':float(worker.total_overtime)})
        set_overtime = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        set_overtime.used = True
        set_overtime.save()
        return HttpResponse(response, content_type='application/json')
