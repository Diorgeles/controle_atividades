from django.urls import path
from .views import home,\
    insert_student, \
    list_student, \
    update_student, \
    delete_student, \
    insert_activity, \
    list_course

urlpatterns = [
    path('', home, name='core_home'),
    path('cadastrar-aluno', insert_student, name='core_insert_student'),
    path('listar-aluno', list_student, name='core_list_student'),
    path('atualizar-aluno/<int:id>', update_student, name='core_update_student'),
    path('excluir-aluno/<int:id>', delete_student, name='core_delete_student'),
    path('cadastrar-curso', insert_activity, name='core_insert_course'),
    path('listar-curso', list_course, name='core_list_course'),

]
