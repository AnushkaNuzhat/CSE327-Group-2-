from unittest import TestCase

from blood_donation.models import BloodRequestModel
from user_control.models import UserModel


class AdviceModelTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(
            email='test4@example.com', name='name', password='asdf123ASDF', is_doctor=True)
        BloodRequestModel.objects.create(user=self.user, patient_name='test_name', gender='test_gender',
                                         blood_group='A+', quantity=2, location='Dhaka', is_emergency=True,
                                         is_active=True, needed_within='2021-09-01', phone='017xxxxxxxx',
                                         note='test_note')

    def test_content(self):
        post = BloodRequestModel.objects.get(id=1)
        expected_object_user = f'{post.user}'
        expected_object_patient_name = f'{post.patient_name}'
        expected_object_gender = f'{post.gender}'
        expected_object_blood_group = f'{post.blood_group}'
        expected_object_quantity = f'{post.quantity}'
        expected_object_location = f'{post.location}'
        expected_object_is_emergency = f'{post.is_emergency}'
        expected_object_is_active = f'{post.is_active}'
        expected_object_needed_within = f'{post.needed_within}'
        expected_object_phone = f'{post.phone}'
        expected_object_note = f'{post.note}'
        self.assertEquals(expected_object_user, self.user.email)
        self.assertEquals(expected_object_patient_name, 'test_name')
        self.assertEquals(expected_object_gender, 'test_gender')
        self.assertEquals(expected_object_blood_group, 'A+')
        self.assertEquals(expected_object_quantity, '2')
        self.assertEquals(expected_object_location, 'Dhaka')
        self.assertEquals(expected_object_is_emergency, 'True')
        self.assertEquals(expected_object_is_active, 'True')
        self.assertEquals(expected_object_needed_within, '2021-09-01')
        self.assertEquals(expected_object_phone, '017xxxxxxxx')
        self.assertEquals(expected_object_note, 'test_note')
