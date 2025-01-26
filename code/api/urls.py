from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, PatientsViewSet


# Создаем роутер для ViewSet
router = DefaultRouter()
router.register(r'patients', PatientsViewSet, basename='patient')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),    # Ручное добавление login в маршруты
    path('', include(router.urls)),    # Включаем маршруты из роутера

]
