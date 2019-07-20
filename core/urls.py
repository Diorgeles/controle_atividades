from django.urls import path, include
from django.contrib.auth import login

from .views import (home, courses,
                    course, activity, activities,
                    register_student)

urlpatterns = [
    path('', home, name='core_home'),
    path('cursos', courses, name='courses'),
    path('cursos/<int:courseId>', course, name='course'),
    path('atividades', activities, name='activities'),
    path('atividades/<int:activityId>', activity, name='activity'),
    path('cadastro_aluno', register_student, name='register_student'),
]
