from django.urls import path  # , include
from .views import CreateCompany, EditCompany

urlpatterns = [
    path('novo/', CreateCompany.as_view(), name='create_company'),
    path('editar/<int:pk>', EditCompany.as_view(), name='edit_company'),
]
