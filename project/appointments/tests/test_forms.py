from django.test import SimpleTestCase
from appointments.views import *


class TestForms(SimpleTestCase):

    def test_PatientAppointmentForm_from_valid_data(self):
        form = PatientAppointmentForm(data={
            'date': "2021-09-01",
            'notes': "test notes",
        })
        self.assertTrue(form.is_valid())

    def test_PatientAppointmentForm_form_no_data(self):
        form = PatientAppointmentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_DoctorAppointmentForm_from_valid_data(self):
        form = DoctorAppointmentForm(data={
            'date': "2021-09-01",
            'time': "12:00",
            'meet_link': "http://www.meet.com",
        })
        self.assertTrue(form.is_valid())

    def test_DoctorAppointmentForm_form_no_data(self):
        form = DoctorAppointmentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_PrescriptionForm_from_valid_data(self):
        form = PrescriptionForm(data={
            'details': "test details",
        })
        self.assertTrue(form.is_valid())

    def test_PrescriptionForm_form_no_data(self):
        form = PrescriptionForm(data={})

        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 0)
