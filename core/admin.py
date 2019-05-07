from django.contrib import admin
from .models import Pergunta, Resposta, Categoria, Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'telefone',
                    'nota', 'porcentagem_acertos', 'aula')


@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('alternativa', 'opcao', 'situacao', 'aula', 'perg')


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('perg', 'aula')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria',)
