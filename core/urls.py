from django.urls import path
from .views import home, insert_student, list_student

urlpatterns = [
    path('', home, name='core_home'),
    path('cadastrar-aluno', insert_student, name='core_insert_student'),
    path('listar-aluno', list_student, name='core_list_student'),
]
