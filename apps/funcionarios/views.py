from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class WorkerList(ListView):
    model = Funcionario

    # sobrescreve a função get_queryset para apresentar somente funcionarios
    # da empresa logada
    def get_queryset(self):
        log_company = self.request.user.funcionario.company
        return Funcionario.objects.filter(company=log_company)


class WorkerEdit(UpdateView):
    model = Funcionario
    fields = ['name', 'departaments']


class WorkerDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_worker')


class WorkerCreate(CreateView):
    model = Funcionario
    fields = ['name', 'departaments']

    def form_valid(self, form):
        worker = form.save(commit=False)
        username = worker.name.split(' ')[0] + worker.name.split(' ')[1]
        worker.company = self.request.user.funcionario.company
        worker.user = User.objects.create(username=username)
        worker.save()

        return super(WorkerCreate, self).form_valid(form)
