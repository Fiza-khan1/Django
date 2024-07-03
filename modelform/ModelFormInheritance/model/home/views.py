from django.shortcuts import render, redirect
from .forms import StudentReg , TeacherReg
from django.http import HttpResponse

def home(request):
    form=StudentReg()
    return render(request, 'home.html',{'form':form})


def student_registration(request):
    if request.method == 'POST':
        form = StudentReg(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Student registration successful.")
    else:
        form = StudentReg()
    
    return render(request, 'home.html', {'form': form})

def teacher_registration(request):
    if request.method == 'POST':
        form = TeacherReg(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Teacher registration successful.")
    else:
        form = TeacherReg()
    
    return render(request, 'teacher_registration.html', {'form': form})

