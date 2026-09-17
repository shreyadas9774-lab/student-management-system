from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'department', 'year', 'email', 'phone_number')
    # Search facility by Name or Department (also added student_id for convenience)
    search_fields = ('name', 'department', 'student_id') 
    list_filter = ('department', 'year')