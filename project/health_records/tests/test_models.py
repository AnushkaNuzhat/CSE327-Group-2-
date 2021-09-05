from unittest import TestCase

from health_records.views import *
from user_control.models import UserModel
from health_records.models import HealthRecordModel


class HealthRecordModelTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='test@example.com', name='name', password='asdf123ASDF')
        self.patient = PatientModel.objects.create(user=self.user)

    def test_content(self):
        post = HealthRecordModel.objects.create(patient=self.patient, title='test_title', content='test_content')
        expected_object_title = f'{post.title}'
        expected_object_content = f'{post.content}'
        self.assertEquals(expected_object_title, 'test_title')
        self.assertEquals(expected_object_content, 'test_content')

    def tearDown(self):
        self.user.delete()
