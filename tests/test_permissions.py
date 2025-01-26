from django.test import TestCase, Client
from datetime import date
from django.urls import reverse
from django.contrib.auth import get_user_model
from api.models import Patient


class PatientAdminTest(TestCase):
    def setUp(self):
        # Создаем суперпользователя
        self.superuser = get_user_model().objects.create_superuser(
            username='admin', password='password'
        )

        # Логинимся как суперпользователь
        logged_in = self.client.login(username='admin', password='password')
        self.assertTrue(logged_in, "Login as superuser failed")

        # Создаем пример пациента
        self.patient = Patient.objects.create(
            date_of_birth=date(1990, 1, 1),
            diagnoses={"flu": "mild"}
        )

    def test_patient_admin_list_display(self):
        # URL списка пациентов в админке
        url = reverse('admin:api_patient_changelist')

        # Выполняем GET-запрос
        response = self.client.get(url)

        # Проверяем статус и контент
        self.assertEqual(response.status_code, 200, f"Unexpected status code: {response.status_code}")
        self.assertContains(response, 'date_of_birth')
        self.assertContains(response, 'diagnoses')


class UserAdminTest(TestCase):
    def setUp(self):
        # Создаем суперпользователя
        self.superuser = get_user_model().objects.create_superuser(
            username='admin', password='password'
        )
        self.client = Client()
        # Логинимся как суперпользователь
        logged_in = self.client.login(username='admin', password='password')
        self.assertTrue(logged_in, "Login as superuser failed")

    def test_user_admin_list_display(self):
        # Проверяем список пользователей в админке
        url = reverse('admin:api_user_changelist')  # Используй правильный путь
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'is_doctor')  # Проверяем отображение 'is_doctor'

    def test_user_admin_add_user(self):
        # Проверяем страницу добавления пользователя
        url = reverse('admin:api_user_add')  # Используй правильный путь
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'is_doctor')  # Проверяем наличие 'is_doctor' в форме

        # Добавляем пользователя
        data = {
            'username': 'doctor_user',
            'password1': 'password123',
            'password2': 'password123',
            'is_doctor': True
        }
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200, "User creation failed")

        # Проверяем, что пользователь создан
        self.assertEqual(get_user_model().objects.filter(username='doctor_user').count(), 1)
        self.assertTrue(get_user_model().objects.get(username='doctor_user').is_doctor)
