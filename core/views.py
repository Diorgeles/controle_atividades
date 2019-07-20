from django.shortcuts import render, redirect
from .models import Students, Course, Activity
from .forms import StudentsForm, CourseForm, ActivityForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required


def home(request):
    template_name = 'base.html'
    return render(request, template_name)


def register_student(request):
    template_name = 'register_student.html'
    if request.method == 'POST':
        user = request.POST['user']
        email = request.POST['email']
        senha = request.POST['senha']
        name = request.POST['name']
        newUser = User.objects.create_user(username=user, email=email, password=senha)
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
