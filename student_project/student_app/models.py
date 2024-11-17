from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    student = models.ForeignKey(Student, related_name="subjects", on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.subject_name} ({self.marks})"
