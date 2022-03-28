from django.urls import path  # , include
from .views import CreateOvertime, ListOvertime

urlpatterns = [
    path('n', CreateOvertime.as_view(), name='create_overtime'),
    path('overtime_list/', ListOvertime.as_view(), name='list_overtime'),

]
