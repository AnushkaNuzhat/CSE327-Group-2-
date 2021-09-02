from django.test import SimpleTestCase
from blood_donation.views import *


class TestForms(SimpleTestCase):

    def test_AddEditPostForm_from_valid_data(self):
        form = BloodRequestForm(data={
            'patient_name': "Name",
            'gender': "Male",
            'blood_group': "A+",
            'quantity': 2,
            'location': "Dhaka",
            'needed_within': "2021-09-01",
            'phone': "01812345678",
        })
        self.assertTrue(form.is_valid())

    def test_AddEditPostForm_form_no_data(self):
        form = BloodRequestForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)
