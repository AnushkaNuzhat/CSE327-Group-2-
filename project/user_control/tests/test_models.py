from django.test import TestCase

from user_control.models import *


class TestUserModel(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(
            email='testuser@gmail.com', name='Test User', password='asdf123ASDF')

    def test_user_email(self):
        user = UserModel.objects.get(id=1)
        expected_object_email = user.email
        self.assertEquals(expected_object_email, 'testuser@gmail.com')

    def test_user_name(self):
        user = UserModel.objects.get(id=1)
        expected_object_name = user.name
        self.assertEquals(expected_object_name, 'Test User')


class TestDoctorModel(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(
            email='testuser@gmail.com', name='Test User', password='asdf123ASDF', is_doctor=True)
        DoctorModel.objects.create(user=self.user, gender="Male", blood_group="AB+", BMDC_regNo='123456789')

    def test_content(self):
        doctor = DoctorModel.objects.get(id=1)
        expected_object_user = f'{doctor.user}'
        expected_object_gender = f'{doctor.gender}'
        expected_object_blood_group = f'{doctor.blood_group}'
        expected_object_BMDC_regNo = f'{doctor.BMDC_regNo}'
        self.assertEquals(expected_object_user, self.user.email)
        self.assertEquals(expected_object_gender, 'Male')
        self.assertEquals(expected_object_blood_group, 'AB+')
        self.assertEquals(expected_object_BMDC_regNo, '123456789')


class PatientModelTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(
            email='testemail@example.com', name='test', password='secret')
        PatientModel.objects.create(user=self.user, gender="Male", blood_group="A+",
                                    phone='+8801812345678')

    def test_content(self):
        patient = PatientModel.objects.get(id=1)
        expected_object_user = f'{patient.user}'
        expected_object_gender = f'{patient.gender}'
        expected_object_blood_group = f'{patient.blood_group}'
        expected_object_phone = f'{patient.phone}'
        self.assertEquals(expected_object_user, self.user.email)
        self.assertEquals(expected_object_gender, 'Male')
        self.assertEquals(expected_object_blood_group, 'A+')
        self.assertEquals(expected_object_phone, '+8801812345678')
