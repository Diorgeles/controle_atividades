from django.db import models


class Aluno(models.Model):

    matricula = models.IntegerField()
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    p_acertos = models.DecimalField(max_digits=3, decimal_places=2)
    aula = models.IntegerField()

    def __str__(self):
        return self.nome


class Categoria(models.Model):

    cat = models.IntegerField()

    def __str__(self):
        return str(self.cat)


class Pergunta(models.Model):

    perg = models.TextField()
    aula = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.perg


class Resposta(models.Model):

    alternativa = models.TextField()
    opcao = models.CharField(max_length=1)
    situacao = models.BooleanField(default=False)
    perg = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    aula = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.alternativa
