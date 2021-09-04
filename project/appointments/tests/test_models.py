from unittest import TestCase

from appointments.models import AppointmentModel
from user_control.models import UserModel, PatientModel, DoctorModel


class AppointmentModelTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(email='testemail@example.com', name='name', password='asdf123ASDF')
        self.patient = PatientModel.objects.create(user=self.user)
        self.doctor = DoctorModel.objects.create(user=self.user)

    def test_content(self):
        appointment = AppointmentModel.objects.create(patient=self.patient, doctor=self.doctor,
                                                      department='test_department',
                                                      date='2021-09-01', time='12:00:00', is_accepted=False,
                                                      is_canceled=False,
                                                      is_complete=False, meet_link='http://www.meet.com',
                                                      notes='test notes')
        expected_object_patient = appointment.patient.user.name
        expected_object_doctor = appointment.doctor.user.name
        expected_object_department = appointment.department
        expected_object_date = appointment.date
        expected_object_time = appointment.time
        expected_object_is_accepted = appointment.is_accepted
        expected_object_is_canceled = appointment.is_canceled
        expected_object_is_complete = appointment.is_complete
        expected_object_meet_link = appointment.meet_link
        expected_object_notes = appointment.notes

        self.assertEquals(expected_object_patient, self.patient.user.name)
        self.assertEquals(expected_object_doctor, self.doctor.user.name)
        self.assertEquals(expected_object_department, 'test_department')
        self.assertEquals(expected_object_date, '2021-09-01')
        self.assertEquals(expected_object_time, '12:00:00')
        self.assertFalse(expected_object_is_accepted)
        self.assertFalse(expected_object_is_canceled)
        self.assertFalse(expected_object_is_complete)
        self.assertEquals(expected_object_meet_link, 'http://www.meet.com')
        self.assertEquals(expected_object_notes, 'test notes')

    def tearDown(self):
        self.user.delete()