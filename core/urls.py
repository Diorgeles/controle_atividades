from django.urls import path
from .views import home,\
    insert_student, \
    list_student, \
    update_student, \
    delete_student, \
    insert_course, \
    list_course, \
    update_course, \
    delete_course, \
    insert_activity, \
    list_activity, \
    update_activity    

urlpatterns = [
    path('', home, name='core_home'),
    path('cadastrar-aluno', insert_student, name='core_insert_student'),
    path('listar-aluno', list_student, name='core_list_student'),
    path('atualizar-aluno/<int:id>', update_student, name='core_update_student'),
    path('excluir-aluno/<int:id>', delete_student, name='core_delete_student'),
    path('cadastrar-curso', insert_course, name='core_insert_course'),
    path('listar-curso', list_course, name='core_list_course'),
    path('atualizar-curso/<int:id>', update_course, name='core_update_course'),
    path('excluir-curso/<int:id>', delete_course, name='core_delete_course'),
    path('cadastrar-atividade', insert_activity, name='core_insert_activity'),
    path('listar-atividade', list_activity, name='core_list_activity'),
    path('atualizar-atividade/<int:id>', update_activity, name='core_update_activity'),

]
