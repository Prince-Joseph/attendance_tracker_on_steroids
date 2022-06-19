from django.db import models

class Department(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    ph_no = models.IntegerField()
    dob = models.IntegerField()
    department = models.ForeignKey(Department,null=True,blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Classroom(models.Model):
    department = models.ForeignKey(Department,null=True,blank=True,on_delete=models.PROTECT)
    year = models.IntegerField()
    section = models.CharField(max_length=30)
    class_Incharge = models.ForeignKey(Teacher,null=True,blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.department.code + str(self.year) + str(self.section)

class Student(models.Model):
    name = models.CharField(max_length=30)
    roll_no = models.CharField(max_length=30)
    classroom = models.ForeignKey(Classroom, null=True,blank=True,on_delete=models.PROTECT)
    department = models.ForeignKey(Department,null=True,blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.roll_no

class Subject(models.Model):
    code = models.CharField(max_length=6)
    full_name = models.CharField(max_length=80)

    def __str__(self):
        return self.full_name

class SubjectTeacher(models.Model):
    """ Subject Dynamic """
    subject = models.ForeignKey(Subject,on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher,null=True,blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.subject.full_name +" " +self.teacher.name
    
class Timetable(models.Model):

    classroom = models.ForeignKey(Classroom, null=True,blank=True,on_delete=models.PROTECT)
    period1 = models.ForeignKey(SubjectTeacher,null=True,blank=True,on_delete=models.PROTECT,related_name='period1')
    period2 = models.ForeignKey(SubjectTeacher,null=True,blank=True,on_delete=models.PROTECT,related_name='period2')
    period3 = models.ForeignKey(SubjectTeacher,null=True,blank=True,on_delete=models.PROTECT,related_name='period3')
    period4 = models.ForeignKey(SubjectTeacher,null=True,blank=True,on_delete=models.PROTECT,related_name='period4')
    period5 = models.ForeignKey(SubjectTeacher,null=True,blank=True,on_delete=models.PROTECT,related_name='period5')
    period6 = models.ForeignKey(SubjectTeacher,null=True,blank=True,on_delete=models.PROTECT,related_name='period6')
    period7 = models.ForeignKey(SubjectTeacher,null=True,blank=True,on_delete=models.PROTECT,related_name='period7')

    def __str__(self):
        return str(self.classroom)

# class Period(models.Model):
#     classroom = models.ForeignKey(SubjectTeacher,null=True,blank=True,on_delete=models.PROTECT) 
#     period = models.IntegerField(default=1,null=True)
#     # def __str__(self):
#       return 
     
class DateWS(models.Model):
    date = models.DateField(unique=True)
    working_day = models.IntegerField(unique=True)
    def __str__(self):
        return str(self.date)

class Attendance(models.Model):
    student = models.ForeignKey(Student,null=True,blank=True,on_delete=models.PROTECT) 
    classroom = models.ForeignKey(Classroom,null=True,blank=True,on_delete=models.PROTECT)  # not required
    working_day = models.ForeignKey(DateWS,on_delete=models.PROTECT)
    period = models.IntegerField(default=1)
    # subject = models.ForeignKey(Subject,null=True,blank=True,on_delete=models.PROTECT) # this thang
    subject_teacher = models.ForeignKey(SubjectTeacher,null=True,blank=True,on_delete=models.PROTECT) # this thang
    def __str__(self):
        return self.student.roll_no + " " + str(self.working_day.date) + " "+ str(self.period) 


    