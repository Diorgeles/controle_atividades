from django.shortcuts import render

def home(request):
    template_name = 'core/base.html'
    return render(request, template_name)
