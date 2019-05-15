from django.shortcuts import render, redirect
from .models import Students
from .forms import StudentsForm


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
