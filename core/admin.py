from django.contrib import admin
from .models import Activity, Course, FinalGrade, Questions, Students, WrongAlternative


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
                    'correct_alternative']
    filter_horizontal = ('wrong_alternative',)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['subscription', 'name']


@admin.register(WrongAlternative)
class WrongAlternativeAdmin(admin.ModelAdmin):
    list_display = ['alternative', 'response']

