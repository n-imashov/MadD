from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from datetime import date
from django.contrib.auth import get_user_model
from api.models import Patient, User


class PatientsViewSetTest(APITestCase):
    def setUp(self):
        self.user_doctor = User.objects.create_user(username="doctor", password="password", is_doctor=True)
        self.user_patient = User.objects.create_user(username="patient", password="password", is_doctor=False)
        self.client = APIClient()

    def test_doctor_can_view_patients(self):
        patient = Patient.objects.create(
            date_of_birth=date(1990, 1, 1),
            diagnoses=["Flu"]
        )
        self.client.force_authenticate(user=self.user_doctor)
        response = self.client.get('/patients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_doctor_cannot_view_patients(self):
        self.client.force_authenticate(user=self.user_patient)
        response = self.client.get('/patients/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], 'Only for doctors.')


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='user', password='password'
        )

    def test_login_success(self):
        response = self.client.post('/login/', {'username': 'user', 'password': 'password'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_invalid(self):
        response = self.client.post('/login/', {'username': 'user', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PatientsViewSetTest(TestCase):
    def setUp(self):
        self.user_doctor = get_user_model().objects.create_user(username='doctor', password='password', is_doctor=True)
        self.user_patient = get_user_model().objects.create_user(username='patient', password='password', is_doctor=False)
        self.client = APIClient()

    def test_patient_list_for_doctor(self):
        patient = Patient.objects.create(
            date_of_birth=date(1990, 1, 1),
            diagnoses=["Flu"]
        )
        self.client.force_authenticate(user=self.user_doctor)
        response = self.client.get('/patients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patient_list_for_non_doctor(self):
        self.client.force_authenticate(user=self.user_patient)
        response = self.client.get('/patients/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], 'Only for doctors.')
