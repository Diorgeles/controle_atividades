from django.db import models
from django.contrib.auth.models import User
from model_utils.models import SoftDeletableModel, TimeStampedModel
import uuid

class Students(SoftDeletableModel, TimeStampedModel):
    """Model definition for Students."""

    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.CharField(max_length=8, default=uuid.uuid4, editable=False)
    name = models.CharField('Nome', max_length=100)

    class Meta:
        """Meta definition for Students."""

        verbose_name = 'Estudante'
        verbose_name_plural = 'Estudantes'

    def __str__(self):
        """Unicode representation of Students."""
        return self.name


class Course(SoftDeletableModel, TimeStampedModel):
    """Model definition for Curso."""

    PERIOD_TYPE = [
        ('morning', 'Manhã'),
        ('afternoon', 'Tarde'),
        ('night', 'Noite'),
    ]

    # TODO: Define fields here
    name = models.CharField('Nome', max_length=100)
    period = models.CharField('Período', max_length=50, choices=PERIOD_TYPE)

    class Meta:
        """Meta definition for Curso."""

        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        """Unicode representation of Curso."""
        return self.name


class Activity(models.Model):
    """Model definition for Activity."""

    # TODO: Define fields here
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time_start = models.DateTimeField(
        'Hora de início', auto_now=False, auto_now_add=False)

    class Meta:
        """Meta definition for Activity."""

        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        """Unicode representation of Activity."""
        return self.course.name


class FinalGrade(models.Model):
    """Model definition for FinalGrade."""

    # TODO: Define fields here
    student = models.ForeignKey(
        Students, verbose_name='Estudante', on_delete=models.CASCADE)
    activity = models.ForeignKey(
        Activity, verbose_name='Atividade', on_delete=models.CASCADE)
    grade = models.DecimalField('Nota', max_digits=5, decimal_places=2)

    class Meta:
        """Meta definition for FinalGrade."""

        verbose_name = 'Nota Final'
        verbose_name_plural = 'Notas Finais'

    def __str__(self):
        """Unicode representation of FinalGrade."""
        return self.student.name


class Questions(models.Model):
    """Model definition for Questions."""

    ALTERNATIVES = [
        ('a', 'A)'),
        ('b', 'B)'),
        ('c', 'C)'),
        ('d', 'D)'),
    ]

    # TODO: Define fields here
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    question = models.TextField()
    value_question = models.DecimalField(
        'Valor da pergunta', max_digits=5, decimal_places=2)
    correct_alternative = models.CharField(
        'Alternativa Correta', max_length=50, choices=ALTERNATIVES)

    class Meta:
        """Meta definition for Questions."""

        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'

    def __str__(self):
        """Unicode representation of Questions."""
        return self.question
