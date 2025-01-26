from datetime import date
from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'date_of_birth', 'diagnoses', 'created_at']

    def validate(self, data):
        # Валидация на уровне нескольких полей
        if data['date_of_birth'] > date.today():
            raise serializers.ValidationError({'date_of_birth': 'Date of birth cannot be in the future.'})

        # Здесь можно добавить другие проверки для других полей, если нужно
        return data