from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase
from datetime import date
from api.serializers import PatientSerializer


class PatientSerializerTest(APITestCase):
    def test_patient_serializer_valid(self):
        patient_data = {
            'date_of_birth': '1990-01-01',
            'diagnoses': ['Flu', 'Cold']
        }
        serializer = PatientSerializer(data=patient_data)
        self.assertTrue(serializer.is_valid())
        patient = serializer.save()
        self.assertEqual(patient.date_of_birth, date(1990, 1, 1))
        self.assertEqual(patient.diagnoses, ['Flu', 'Cold'])

    def test_patient_serializer_invalid(self):
        invalid_data = {
            'date_of_birth': 'invalid_date',
            'diagnoses': 'invalid_diagnoses'
        }
        serializer = PatientSerializer(data=invalid_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

