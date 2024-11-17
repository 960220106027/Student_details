from django import forms
from .models import Student, Subject

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Name'}),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'marks']
        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject Name'}),
            'marks': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Marks'}),
        }
