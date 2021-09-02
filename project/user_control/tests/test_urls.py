from django.test import SimpleTestCase
from django.urls import reverse, resolve

from user_control.views import *


class TestUrls(SimpleTestCase):

    def test_home_view_url_is_resolved(self):
        url = reverse('home')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, home_view)

    def test_login_view_url_is_resolved(self):
        url = reverse('login')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, login_view)

    def test_doctor_signup_view_url_is_resolved(self):
        url = reverse('doctor-register')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, doctor_signup_view)

    def test_patient_signup_view_url_is_resolved(self):
        url = reverse('patient-register')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, patient_signup_view)

    def test_doctor_dashboard_url_is_resolved(self):
        url = reverse('doctor-dashboard')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, doctor_dashboard)

    def test_patient_dashboard_url_is_resolved(self):
        url = reverse('patient-dashboard')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, patient_dashboard)

    def test_doctor_profile_view_url_is_resolved(self):
        url = reverse('doctor-profile', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, doctor_profile_view)

    def test_patient_profile_view_url_is_resolved(self):
        url = reverse('patient-profile', args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, patient_profile_view)

    def test_doctor_edit_profile_url_is_resolved(self):
        url = reverse('doctor-edit-profile')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, doctor_edit_profile)

    def test_patient_edit_profile_url_is_resolved(self):
        url = reverse('patient-edit-profile')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, patient_edit_profile)

    def test_account_settings_view_url_is_resolved(self):
        url = reverse('account-settings')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, account_settings_view)

    def test_contact_view_url_is_resolved(self):
        url = reverse('contact')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, contact_view)
