from django.urls import path
from .views import NewDocument, DeleteDocument

urlpatterns = [
    path('new/<int:worker_id>/', NewDocument.as_view(), name='new_document'),
    path('delete/<int:pk>/', DeleteDocument.as_view(), name='delete_document'),
]
