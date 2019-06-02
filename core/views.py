from django.shortcuts import render, redirect
from .models import Students, Course, Activity
from .forms import StudentsForm, CourseForm, ActivityForm


def home(request):
    template_name = 'base.html'
    return render(request, template_name)


def students(request):
    """This view is reponsible for creating and listing"""
    template_name = 'student.html'
    form = StudentsForm(request.POST or None)
    students = Students.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('students')
    return render(request, template_name, locals())


def student(request, studentId):
    """This view is reponsible for updating and deleting"""
    template_name = 'student.html'
    student = Students.objects.get(id=studentId)
    students = Students.objects.all()
    form = StudentsForm(request.POST or None, instance=student)
    if request.method == 'POST':
        if 'SAVE' in request.POST:
            if form.is_valid():
                form.save()
        if 'DELETE' in request.POST:
            student.delete()
        return redirect('students')
    return render(request, template_name, locals())


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
