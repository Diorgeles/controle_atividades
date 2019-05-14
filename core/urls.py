from django.urls import path
from .views import home, insert_student

urlpatterns = [
    path('', home, name='core_home'),
    path('cadastrar-aluno', insert_student, name='core_insert_student'),
]
