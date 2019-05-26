from django.shortcuts import render, redirect
from .models import Students, Course, Activity
from .forms import StudentsForm, CourseForm, ActivityForm


def home(request):
    template_name = 'core/base.html'
    return render(request, template_name)


def insert_student(request):
    form = StudentsForm(request.POST or None)
    template_name = 'core/insert_student.html'

    if form.is_valid():
        form.save()
        return redirect('core_home')
    return render(request, template_name, {'form': form})


def list_student(request):
    student = Students.objects.all()
    template_name = 'core/list_student.html'
    return render(request, template_name, {'student': student})


def update_student(request, id):
    data = {}
    template_name = 'core/update_student.html'
    student = Students.objects.get(id=id)
    form = StudentsForm(request.POST or None, instance=student)
    data['student'] = student
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_list_student')
    return render(request, template_name, data)


def delete_student(request, id):
    student = Students.objects.get(id=id)
    template_name = 'core/delete_confirm.html'
    if request.method == 'POST':
        student.delete()
        return redirect('core_list_student')
    else:
        return render(request, template_name, {'obj': student})


def insert_course(request):
    form = CourseForm(request.POST or None)
    template_name = 'core/insert_course.html'

    if form.is_valid():
        form.save()
        form = CourseForm()
        msg = 'true'
        return render(request, template_name, {'form': form, 'msg': msg})
    return render(request, template_name, {'form': form})


def list_course(request):
    course = Course.objects.all()
    template_name = 'core/list_course.html'
    return render(request, template_name, {'course': course})


def update_course(request, id):
    data = {}
    template_name = 'core/update_course.html'
    course = Course.objects.get(id=id)
    form = CourseForm(request.POST or None, instance=course)
    data['course'] = course
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_list_course')
    return render(request, template_name, data)


def delete_course(request, id):
    course = Course.objects.get(id=id)
    template_name = 'core/delete_confirm.html'

    if request.method == 'POST':
        course.delete()
        return redirect('core_list_course')
    else:
        return render(request, template_name, {'obj': course})


def insert_activity(request):
    form = ActivityForm(request.POST or None)
    template_name = 'core/insert_activity.html'

    if form.is_valid():
        form.save()
        form = CourseForm()
        msg = 'true'
        return render(request, template_name, {'form': form, 'msg': msg})
    return render(request, template_name, {'form': form})


def list_activity(request):
    activity = Activity.objects.all()
    template_name = 'core/list_activity.html'
    return render(request, template_name, {'activity': activity})


def update_activity(request, id):
    data = {}
    template_name = 'core/update_activity.html'
    activity = Activity.objects.get(id=id)
    form = ActivityForm(request.POST or None, instance=activity)
    data['activity'] = activity
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_list_activity')
    return render(request, template_name, data)
