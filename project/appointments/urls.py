from django.urls import path

from .views import *

urlpatterns = [
    path('', patient_appointment_home_view, name='patient-appointment-home'),
    path('home', doctor_appointment_home_view, name='doctor-appointment-home'),
    path('appointment/<str:pk>', appointment_detail_view, name='appointment-details'),
    path('make-appointment/<int:pk>', make_appointment_view, name='make-appointment'),
    path('appointment/<int:pk>/update', doctor_appointment_update_view, name='doctor-appointment-update'),
    path('update/<int:pk>', patient_appointment_update_view, name='patient-appointment-update'),
    path('appointment/<int:pk>/delete', appointment_delete_view, name='appointment-delete'),
    path('appointment/<int:pk>/reject', appointment_reject_view, name='appointment-reject'),
    path('doctors', appointment_doctor_list_view, name='appointment-doctors-list'),

    path('write-prescription/<int:pk>', write_prescription_view, name='write-prescription'),
    path('download-prescription/<str:pk>', pdf_view, name='pdf-view'),
]
