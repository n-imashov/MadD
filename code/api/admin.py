from django.contrib import admin
from .models import User, Patient
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Создаем класс для настройки отображения модели User в админке
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'is_doctor')     # Поля, которые будут отображаться
    list_filter = ()     # Фильтрация по полю is_doctor

    # Настройка формы создания нового пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'is_doctor', 'password1', 'password2', ),  # Добавляем is_doctor в форму
        }),
    )

    # Настройка формы редактирования пользователя
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'is_doctor', 'password'),
        }),
    )

# Регистрируем модель пользователя с изменениями в админке
admin.site.register(User, UserAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_birth', 'diagnoses', 'created_at')

admin.site.register(Patient, PatientAdmin)
