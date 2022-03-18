from django.urls import path  # , include
from .views import home, FuncionariosList

urlpatterns = [
    path('', home),
    path('funcionarios/', FuncionariosList.as_view(), name='list_worker'),
]
