from django.shortcuts import render, redirect
from .models import Students, Course, Activity, Questions, WrongAlternative
from .forms import StudentsForm, CourseForm, ActivityForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    template_name = 'base.html'
    return render(request, template_name)


@login_required()
def register_student(request):
    template_name = 'register_student.html'
    if request.method == 'POST':
        user = request.POST['user']
        email = request.POST['email']
        senha = request.POST['senha']
        name = request.POST['name']
        newUser = User.objects.create_user(
            username=user, email=email, password=senha)
        newUser.save()
        student = Students.objects.create(user=newUser, name=name)
        my_group = Group.objects.get(name='aluno')
        my_group.user_set.add(newUser)
        msg = 'true'

        return render(request, template_name, locals())
    return render(request, template_name, locals())


@login_required()
def courses(request):
    """This view is reponsible for creating and listing"""
    template_name = 'course.html'
    form = CourseForm(request.POST or None)
    courses = Course.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('courses')
    return render(request, template_name, locals())


@login_required()
def course(request, courseId):
    """This view is reponsible for updating and deleting"""
    template_name = 'course.html'
    course = Course.objects.get(id=courseId)
    courses = Course.objects.all()
    form = CourseForm(request.POST or None, instance=course)

    if request.method == 'POST':
        if 'SAVE' in request.POST:
            if form.is_valid():
                form.save()
        if 'DELETE' in request.POST:
            course.delete()
        return redirect('courses')
    return render(request, template_name, locals())


@login_required()
def activities(request):
    """This view is reponsible for creating and listing"""
    template_name = 'activity.html'
    form = ActivityForm(request.POST or None)
    activities = Activity.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('activities')
    return render(request, template_name, locals())


@login_required()
def activity(request, activityId):
    """This view is reponsible for updating and deleting"""
    template_name = 'activity.html'
    activity = Activity.objects.get(id=activityId)
    activities = Activity.objects.all()
    form = ActivityForm(request.POST or None, instance=activity)

    if request.method == 'POST':
        if 'SAVE' in request.POST:
            if form.is_valid():
                form.save()
        if 'DELETE' in request.POST:
            activity.delete()
        return redirect('activities')
    return render(request, template_name, locals())


def questions(request):
    """This view is reponsible for creating and listing"""
    activities = Activity.objects.all()
    template_name = 'question.html'

    # faço uma lista simples com todas as letras possiveis, ela basicamente será usada para marcar as respostas erradas
    alternatives = ['a', 'b', 'c', 'd']

    if request.method == 'POST':
        if 'SAVE' in request.POST:
            activity_id = request.POST['activity']
            question = request.POST['question']
            value_question = request.POST['value_question']
            response = request.POST['response']
            correct_alternative = request.POST['correct_alternative']

            # desse jeito eu consigo pegar uma lista de objetos que vem no request
            # a sacada por tras do envio de lista pelo request, está no macete de vc colocar
            # os campos que vc quer como lista tem que ter todos o mesmo "name" no html
            # observe que existe 3 campos para resposta errada e os 3 ta com mesmo "name" e "id"
            # com isso o retorno no request vem em uma lista
            wrong_responses = request.POST.getlist('wrong_response')

            # Removo a letra que foi escolhida para a resposta correta
            alternatives.remove(correct_alternative)

            # quando eu seleciono uma atividade é enviado o id de tal atividade
            activity = Activity.objects.get(id=activity_id)

            # Crio um instancia do questions e monto todo o objeto com o que vem do request
            quest = Questions()
            quest.activity = activity
            quest.question = question
            quest.value_question = value_question
            quest.response = response
            quest.correct_alternative = correct_alternative
            quest.save()

            # esse enumerate serve pra retornar o valor da lista + um index, ele é bom pra situações
            # que vc vai precisar de um "contador"
            for index, wrong_response in enumerate(wrong_responses):
                wrong = WrongAlternative()
                wrong.response = wrong_response
                wrong.alternative = alternatives[index]
                wrong.activity = activity
                wrong.save()
                # essa é a forma de vc inserir valor em um campo manytomany
                quest.wrong_alternative.add(wrong)

    return render(request, template_name, locals())
