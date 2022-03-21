
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Departamento
# Create your views here.


class DepartamentList(ListView):
    model = Departamento
    fields = ['name']

    def get_queryset(self):
        # lista somente departamentos da empresa logada
        log_company = self.request.user.funcionario.company
        return Departamento.objects.filter(company=log_company)


class DepartamentNew(CreateView):
    model = Departamento
    fields = ['name']

    def form_valid(self, form):
        departament = form.save(commit=False)
        departament.company = self.request.user.funcionario.company
        departament.save()
        return super(DepartamentNew, self).form_valid(form)


class DepartamentEdit(UpdateView):
    model = Departamento
    fields = ['name']


class DepartamentDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departament')
