from django.urls import path
from .views import (
    DepartamentList,
    DepartamentNew,
    DepartamentEdit,
    DepartamentDelete)

urlpatterns = [
    path('', DepartamentList.as_view(), name='list_departament'),
    path('new', DepartamentNew.as_view(), name='new_departament'),
    path('edit/<int:pk>', DepartamentEdit.as_view(), name='edit_departament'),
    path('delete/<int:pk>', DepartamentDelete.as_view(),
         name='delete_departament'),
]
