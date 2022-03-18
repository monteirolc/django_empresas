# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

# Create your views here.


def home(request):
    return HttpResponse('olá')


class FuncionariosList(ListView):

    return
