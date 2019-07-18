from django.urls import path

from .views import (home, courses,
                    course, activity, activities,
                    register_student, home_student)

urlpatterns = [
    path('', home, name='core_home'),
    path('cursos', courses, name='courses'),
    path('cursos/<int:courseId>', course, name='course'),
    path('atividades', activities, name='activities'),
    path('atividades/<int:activityId>', activity, name='activity'),
    path('cadastro_aluno', register_student, name='register_student'),
    path('home_aluno', home_student, name='home_student'),
]
