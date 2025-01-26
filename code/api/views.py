from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from .serializers import PatientSerializer


class LoginView(TokenObtainPairView):
    pass  # Наследуемся от готового класса


class PatientsViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):   # Если пользователь не является врачом, возвращаем предупреждение.
        if not request.user.is_doctor:
            return Response(
                {'detail': 'Only for doctors.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().list(request, *args, **kwargs)
