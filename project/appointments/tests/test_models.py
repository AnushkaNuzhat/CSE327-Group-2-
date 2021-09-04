from unittest import TestCase

from appointments.models import AppointmentModel
from user_control.models import UserModel, PatientModel, DoctorModel


class AppointmentModelTest(TestCase):

    def setUp(self):
        # Creating a user type object
        self.user = UserModel.objects.create_user(email='testemail@example.com', name='name', password='asdf123ASDF')
        # Creating a patient type object
        self.patient = PatientModel.objects.create(user=self.user)
        # Creating a doctor type object
        self.doctor = DoctorModel.objects.create(user=self.user)

    # Function to test if the appointment model is created
    def test_content(self):
        # Creating an appointment type object
        appointment = AppointmentModel.objects.create(patient=self.patient, doctor=self.doctor,
                                                      department='test_department',
                                                      date='2021-09-01', time='12:00:00', is_accepted=False,
                                                      is_canceled=False,
                                                      is_complete=False, meet_link='http://www.meet.com',
                                                      notes='test notes')
        expected_object_patient = appointment.patient.user.name # Expected patient name
        expected_object_doctor = appointment.doctor.user.name # Expected doctor name
        expected_object_department = appointment.department # Expected department name
        expected_object_date = appointment.date # Expected date
        expected_object_time = appointment.time # Expected time
        expected_object_is_accepted = appointment.is_accepted # Expected is_accepted value
        expected_object_is_canceled = appointment.is_canceled # Expected is_canceled value
        expected_object_is_complete = appointment.is_complete # Expected is_complete value
        expected_object_meet_link = appointment.meet_link # Expected meet_link value
        expected_object_notes = appointment.notes # Expected notes value

        self.assertEquals(expected_object_patient, self.patient.user.name) # Testing if the patient name is correct
        self.assertEquals(expected_object_doctor, self.doctor.user.name) # Testing if the doctor name is correct
        self.assertEquals(expected_object_department, 'test_department') # Testing if the department name is correct
        self.assertEquals(expected_object_date, '2021-09-01') # Testing if the date is correct
        self.assertEquals(expected_object_time, '12:00:00') # Testing if the time is correct
        self.assertFalse(expected_object_is_accepted) # Testing if the is_accepted value is correct
        self.assertFalse(expected_object_is_canceled) # Testing if the is_canceled value is correct
        self.assertFalse(expected_object_is_complete) # Testing if the is_complete value is correct
        self.assertEquals(expected_object_meet_link, 'http://www.meet.com') # Testing if the meet_link value is correct
        self.assertEquals(expected_object_notes, 'test notes') # Testing if the notes value is correct

    # Function to delete the previously crested user
    def tearDown(self):
        self.user.delete()