from django.urls import path  # , include
from .views import WorkerList, WorkerEdit, WorkerDelete, WorkerCreate

urlpatterns = [
    path('', WorkerList.as_view(), name='list_worker'),
    path('edit/<int:pk>', WorkerEdit.as_view(), name='update_worker'),
    path('delete/<int:pk>', WorkerDelete.as_view(), name='delete_worker'),
    path('new/', WorkerCreate.as_view(), name='create_worker'),


]
