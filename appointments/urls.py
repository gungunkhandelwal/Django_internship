from django.urls import path
from . views import *

urlpatterns=[
    path('doctor_list/',doctor_list,name='doctor_list'),
    path('book_appointment/<int:doctor_id>/',book_appointment,name='book_appointment'),
    path('appointment_details/<int:appointment_id>/',appointment_details, name='appointment_details'),
]