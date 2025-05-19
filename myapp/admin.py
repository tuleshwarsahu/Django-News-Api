from django.contrib import admin
from .models import Teacher, Articles

admin.site.register(Articles)
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'basic_salary', 'hra_enabled', 'hra_amount', 'gross_salary']
    readonly_fields = ['hra_amount', 'gross_salary']

