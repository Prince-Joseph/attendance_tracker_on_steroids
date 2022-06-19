from django.shortcuts import render
from .models import Attendance

# Create your views here.
def index(request):
    
    all_objects = Attendance.objects.all()
    prince_purana = all_objects.filter(student=1).filter(subject_teacher = 1).filter(subject_teacher = 4)
    # subject_teacher  class date period 
    # subject = form.cleaned['subject'] # "ada" 
    # teacher = form.cleaned['teacher'] # "ada" 
    # SBT = SEACHER()--> 9D

    ada_class_15 = all_objects.filter(classroom=1).filter(subject_teacher=1).filter(working_day=1).filter(period=1)
    print(ada_class_15)
    # print(prince_purana_at_pcc)
    
    context={
        'anna': prince_purana,
        'asa': ada_class_15,
    }
    
    context['data'] = prince_purana
    
    return render(request,"index.html",context)