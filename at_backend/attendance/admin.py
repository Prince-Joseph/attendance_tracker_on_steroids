from django.contrib import admin
from .models import  Classroom, DateWS,
                    Department,Subject,SubjectTeacher,Timetable,Teacher,Student,Attendance

admin.site.register(Classroom)
admin.site.register(DateWS)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(SubjectTeacher)
admin.site.register(Timetable)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Attendance)
