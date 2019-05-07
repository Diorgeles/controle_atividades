from django.contrib import admin
from .models import Activity, Course, FinalGrade, Questions, Students


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['course', 'time_start']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'period']


@admin.register(FinalGrade)
class FinalGradeAdmin(admin.ModelAdmin):
    list_display = ['student', 'activity', 'grade']


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['activity', 'question', 'value_question',
                    'alternatives', 'correct_alternative']


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['subscription', 'name']
