from django.views.generic import CreateView, DeleteView
from .models import Documento
from django.urls import reverse_lazy


class NewDocument(CreateView):
    model = Documento
    fields = ['description', 'file']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.belongs_to_id = self.kwargs['worker_id']
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tudo"] = Documento.objects.all()
        return context


class DeleteDocument(DeleteView):
    model = Documento
    success_url = reverse_lazy('list_worker')
