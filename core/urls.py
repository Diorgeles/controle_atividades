from django.urls import path

from .views import (home, students, student, courses,
                    course, activity, activities)

urlpatterns = [
    path('', home, name='core_home'),
    path('alunos', students, name='students'),
    path('alunos/<int:studentId>', student, name='student'),
    path('cursos', courses, name='courses'),
    path('cursos/<int:courseId>', course, name='course'),
    path('atividades', activities, name='activities'),
    path('atividades/<int:activityId>', activity, name='activity')
]
