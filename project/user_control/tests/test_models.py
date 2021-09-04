from django.test import TestCase

from user_control.models import *


class TestUserModel(TestCase):

    def setUp(self):
        # Creating a user type object
        self.user = UserModel.objects.create(
            email='testuser@gmail.com', name='Test User', password='asdf123ASDF')

    # Test for user's email
    def test_user_email(self):
        expected_object_email = self.user.email
        self.assertEquals(expected_object_email, 'testuser@gmail.com')

    # Test for user's name
    def test_user_name(self):
        expected_object_name = self.user.name
        self.assertEquals(expected_object_name, 'Test User')

    # Deleting previously created user type object
    def tearDown(self):
        self.user.delete()


class TestDoctorModel(TestCase):

    def setUp(self):
        # Creating a user type object
        self.user = UserModel.objects.create(
            email='testuser@gmail.com', name='Test User', password='asdf123ASDF', is_doctor=True)
        # Creating a doctor type object
        self.doctor = DoctorModel.objects.create(user=self.user, gender="Male", blood_group="AB+",
                                                 BMDC_regNo='123456789')

    # Testing the contents of created object
    def test_content(self):
        doctor = self.doctor
        expected_object_gender = doctor.gender
        expected_object_blood_group = doctor.blood_group
        expected_object_BMDC_regNo = doctor.BMDC_regNo
        self.assertEquals(expected_object_gender, 'Male')
        self.assertEquals(expected_object_blood_group, 'AB+')
        self.assertEquals(expected_object_BMDC_regNo, '123456789')

    # Deleting previously created user type object
    def tearDown(self):
        self.user.delete()


class PatientModelTest(TestCase):

    def setUp(self):
        # Creating a user type object
        self.user = UserModel.objects.create(
            email='testemail@example.com', name='test', password='secret')
        # Creating a patient type object
        self.patient = PatientModel.objects.create(user=self.user, gender="Male", blood_group="A+",
                                                   phone='+8801812345678')

    # Testing the contents of created object
    def test_content(self):
        patient = self.patient
        expected_object_gender = patient.gender
        expected_object_blood_group = patient.blood_group
        expected_object_phone = patient.phone
        self.assertEquals(expected_object_gender, 'Male')
        self.assertEquals(expected_object_blood_group, 'A+')
        self.assertEquals(expected_object_phone, '+8801812345678')

    # Deleting previously created user type object
    def tearDown(self):
        self.user.delete()
