from django.contrib import admin
from .models import Pergunta, Resposta, Categoria, Aluno


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'telefone', 'nota', 'porcentagem_acertos', 'aula')


class RespostaAdmin(admin.ModelAdmin):
    list_display = ('alternativa', 'opcao', 'situacao', 'aula', 'perg')


class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('perg', 'aula')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria',)

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Resposta, RespostaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
