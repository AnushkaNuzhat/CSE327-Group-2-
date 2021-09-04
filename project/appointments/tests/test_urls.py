from django.test import SimpleTestCase
from django.urls import reverse, resolve
from appointments.views import *


class TestUrls(SimpleTestCase):

    def test_patient_appointment_home_view_url_is_resolved(self):
        url = reverse('patient-appointment-home')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, patient_appointment_home_view)

    def test_doctor_appointment_home_view_url_is_resolved(self):
        url = reverse('doctor-appointment-home')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, doctor_appointment_home_view)

    def test_appointment_detail_view_url_is_resolved(self):
        url = reverse('appointment-details', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, appointment_detail_view)

    def test_make_appointment_view_url_is_resolved(self):
        url = reverse('make-appointment', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, make_appointment_view)

    def test_doctor_appointment_update_view_url_is_resolved(self):
        url = reverse('doctor-appointment-update', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, doctor_appointment_update_view)

    def test_patient_appointment_update_view_url_is_resolved(self):
        url = reverse('patient-appointment-update', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, patient_appointment_update_view)

    def test_appointment_delete_view_url_is_resolved(self):
        url = reverse('appointment-delete', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, appointment_delete_view)

    def test_appointment_reject_view_url_is_resolved(self):
        url = reverse('appointment-reject', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, appointment_reject_view)

    def test_appointment_doctor_list_view_url_is_resolved(self):
        url = reverse('appointment-doctors-list')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, appointment_doctor_list_view)

    def test_write_prescription_view_url_is_resolved(self):
        url = reverse('write-prescription', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, write_prescription_view)

    def test_pdf_view_url_is_resolved(self):
        url = reverse('pdf-view', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, pdf_view)
