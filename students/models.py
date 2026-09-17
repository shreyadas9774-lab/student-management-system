from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True, help_text="e.g., STU1024")
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.IntegerField(help_text="Enter year (1-4)")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_id} - {self.name}"