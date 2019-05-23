from django import forms
from .models import Students, Course

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
