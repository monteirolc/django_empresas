from django.urls import path  # , include
from .views import CreateOvertime, ListOvertime, ChangeOvertime, DeleteOvertime

urlpatterns = [
    path('new', CreateOvertime.as_view(), name='create_overtime'),
    path('overtime_list/', ListOvertime.as_view(), name='list_overtime'),
    path('change_overtime/<int:pk>/', ChangeOvertime.as_view(), name='edit_overtime'),
    path('delete_overtime/<int:pk>/', DeleteOvertime.as_view(), name='delete_overtime'),

]
