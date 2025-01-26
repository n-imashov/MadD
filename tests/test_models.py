from django.test import TestCase
from datetime import date

from api.models import Patient
from api.serializers import PatientSerializer


class PatientModelTest(TestCase):
    def test_patient_creation(self):
        patient = Patient.objects.create(
            date_of_birth=date(1990, 1, 1),
            diagnoses=["Flu", "Cold"]
        )
        self.assertEqual(patient.date_of_birth, date(1990, 1, 1))
        self.assertEqual(patient.diagnoses, ["Flu", "Cold"])
        self.assertIsInstance(patient.created_at, type(patient.created_at))

    def test_patient_creation_with_valid_data(self):
        data = {
            'date_of_birth': date(1990, 1, 1),
            'diagnoses': ['Flu', 'Cold']
        }
        serializer = PatientSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        patient = serializer.save()
        self.assertEqual(patient.date_of_birth, date(1990, 1, 1))
        self.assertEqual(patient.diagnoses, ['Flu', 'Cold'])

    def test_patient_creation_with_invalid_date_of_birth(self):
        data = {
            'date_of_birth': date(3000, 1, 1),  # Неверная дата
            'diagnoses': ['Flu']
        }
        serializer = PatientSerializer(data=data)
        self.assertFalse(serializer.is_valid())  # Ожидаем, что сериализатор не пройдет валидацию
        self.assertIn('date_of_birth', serializer.errors)  # Проверяем, что ошибка на поле date_of_birth
        self.assertEqual(serializer.errors['date_of_birth'][0], 'Date of birth cannot be in the future.')

