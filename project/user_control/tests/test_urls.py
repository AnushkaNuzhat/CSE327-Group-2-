from django.test import SimpleTestCase
from django.urls import reverse, resolve

from user_control.views import *


class TestUrls(SimpleTestCase):

    # Test the url for the Home page/view
    def test_home_view_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home_view)

    # Test the url for the login page/view
    def test_login_view_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_view)

    # Test the url for the doctor register page/view
    def test_doctor_signup_view_url_is_resolved(self):
        url = reverse('doctor-register')
        self.assertEquals(resolve(url).func, doctor_signup_view)

    # Test the url for the patient register page/view
    def test_patient_signup_view_url_is_resolved(self):
        url = reverse('patient-register')
        self.assertEquals(resolve(url).func, patient_signup_view)

    # Test the url for the doctor dashboard page/view
    def test_doctor_dashboard_url_is_resolved(self):
        url = reverse('doctor-dashboard')
        self.assertEquals(resolve(url).func, doctor_dashboard)

    # Test the url for the patient dashboard page/view
    def test_patient_dashboard_url_is_resolved(self):
        url = reverse('patient-dashboard')
        self.assertEquals(resolve(url).func, patient_dashboard)

    # Test the url for doctor profile page/view
    def test_doctor_profile_view_url_is_resolved(self):
        url = reverse('doctor-profile', args=[1])
        self.assertEquals(resolve(url).func, doctor_profile_view)

    # Test the url for patient profile page/view
    def test_patient_profile_view_url_is_resolved(self):
        url = reverse('patient-profile', args=[1])
        self.assertEquals(resolve(url).func, patient_profile_view)

    # Test the url for doctor edit profile page/view
    def test_doctor_edit_profile_url_is_resolved(self):
        url = reverse('doctor-edit-profile')
        self.assertEquals(resolve(url).func, doctor_edit_profile)

    # Test the url for patient edit profile page/view
    def test_patient_edit_profile_url_is_resolved(self):
        url = reverse('patient-edit-profile')
        self.assertEquals(resolve(url).func, patient_edit_profile)

    # Test the url for account settings pa
    def test_account_settings_view_url_is_resolved(self):
        url = reverse('account-settings')
        self.assertEquals(resolve(url).func, account_settings_view)

    # Test the url for contact page/view
    def test_contact_view_url_is_resolved(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact_view)
