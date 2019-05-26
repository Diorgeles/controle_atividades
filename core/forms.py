from django import forms
from .models import Students, Course, Activity

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'