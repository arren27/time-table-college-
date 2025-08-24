# timetable_backend/timetable_app/models.py
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TimetableEntry(models.Model):
    TE_TYPE_CHOICES = [
        ('Lecture', 'Lecture'),
        ('Lab', 'Lab'),
        ('Break', 'Break'),
        ('Relieve', 'Relieve'),
    ]
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    entry_type = models.CharField(max_length=10, choices=TE_TYPE_CHOICES)
    day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.entry_type} - {self.subject} by {self.teacher} on {self.day}"

