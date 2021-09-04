from django.test import TestCase

from user_control.forms import *


class TestForms(TestCase):
    #  Valid data to create a doctor type user
    doctor_valid_data = {
        'email': 'doctor@gmail.com',
        'name': 'Doctor',
        'password1': 'asdf123ASDF',
        'password2': 'asdf123ASDF',
        'check': True,
    }
    # Invalid data to create a doctor type user
    doctor_invalid_data = {
        'email': 'doctor@gmail.com',
        'name': '',
        'password1': 'asdf123ASDF',
        'password2': 'asdf123ASDF',
        'check': True,
    }
    # Valid data to create a patient type user
    patient_valid_data = {
        'email': 'patient@gmail.com',
        'name': 'Patient',
        'password1': 'asdf123ASDF',
        'password2': 'asdf123ASDF',
        'check': True,
    }
    # Invalid data to create a patient type user
    patient_invalid_data = {
        'email': 'patient@.com',
        'name': '',
        'password1': 'asdf123ASDF',
        'password2': 'asdf123ASDF',
        'check': True,
    }

    # Testing doctor registration form with valid data
    def test_doctor_registration_form_with_valid_data(self):
        form = DoctorRegistrationForm(data=self.doctor_valid_data)
        self.assertTrue(form.is_valid())

    # Testing doctor registration form with invalid data
    def test_doctor_registration_form_with_invalid_data(self):
        form = DoctorRegistrationForm(data=self.doctor_invalid_data)
        self.assertFalse(form.is_valid())

    # Testing patient registration form with valid data
    def test_patient_registration_form_with_valid_data(self):
        form = PatientRegistrationForm(data=self.patient_valid_data)
        self.assertTrue(form.is_valid())

    # Testing patient registration form with invalid data
    def test_patient_registration_form_with_invalid_data(self):
        form = PatientRegistrationForm(data=self.patient_invalid_data)
        self.assertFalse(form.is_valid())
