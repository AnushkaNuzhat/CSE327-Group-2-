from django.test import SimpleTestCase
from appointments.views import *


class TestForms(SimpleTestCase):

    # Test the form for adding a new appointment with valid data
    def test_PatientAppointmentForm_from_valid_data(self):
        form = PatientAppointmentForm(data={
            'date': "2021-09-01",
            'notes': "test notes",
        })# testing with data
        self.assertTrue(form.is_valid()) # no errors if the form is valid

    # Test the form for adding a new appointment with invalid data
    def test_PatientAppointmentForm_form_no_data(self):
        form = PatientAppointmentForm(data={}) # no data to test

        self.assertFalse(form.is_valid()) # errors will be shown if the form is invalid
        self.assertEqual(len(form.errors), 1) # 1 error will be shown

    # Test the form for adding a new appointment with valid data
    def test_DoctorAppointmentForm_from_valid_data(self):
        form = DoctorAppointmentForm(data={
            'date': "2021-09-01",
            'time': "12:00",
            'meet_link': "http://www.meet.com",
        }) # testing with data
        self.assertTrue(form.is_valid()) # no errors if the form is valid

    # Test the form for adding a new appointment with invalid data
    def test_DoctorAppointmentForm_form_no_data(self):
        form = DoctorAppointmentForm(data={}) # no data to test

        self.assertFalse(form.is_valid()) # errors will be shown if the form is invalid
        self.assertEqual(len(form.errors), 3) # 3 errors will be shown if the form is invalid

    # Test the form for adding a new prescription with valid data
    def test_PrescriptionForm_from_valid_data(self):
        form = PrescriptionForm(data={
            'details': "test details",
        }) # testing with data
        self.assertTrue(form.is_valid()) # no errors if the form is valid

    # Test the form for adding a new prescription with invalid data
    def test_PrescriptionForm_form_no_data(self):
        form = PrescriptionForm(data={}) # no data to test

        self.assertTrue(form.is_valid()) # errors will be shown if the form is invalid
        self.assertEqual(len(form.errors), 0) # 0 errors will be shown if the form is invalid
