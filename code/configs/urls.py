from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Для доступа к админке
    path('', include('api.urls')),  # Подключаем маршруты из приложения `api`
]
