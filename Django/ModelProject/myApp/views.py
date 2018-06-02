from django.shortcuts import render
from .models import Student,Grades

# Create your views here.
from django.http import HttpResponse
def index(request):
    # return HttpResponse("This is the mainpage of myApp!!!")
    return render(request,'myApp/myAppindex.html')

def news(req):
    return HttpResponse("News News News!!!")

def addStudent(req):
    grade = Grades.objects.get(pk=1)
    stu = Student.createStudent("刘德华",34,True,"我叫刘德华",
                                grade,"2018-4-18","2018-4-16")
    stu.save()
    return HttpResponse("ADD OK!")
def addStudent2(request):
    grade = Grades.objects.get(pk=1)
    stu = Student.stuObj2.createStudnet("张学友",55,True,"我叫张学友，凯哥帅", grade, "2017-8-10", "2017-8-11")
    stu.save()
    return HttpResponse("*********")

def getStudents(req):
    s = Student.stuObj2.all().filter(sage=18).count()
    return HttpResponse(s)
def students0(req):
    s = Student.stuObj2.all()[0:2]
    return HttpResponse(s.values())
def stupage(req,page):
    page = int(page)
    if page <= 0:
        page = 1
    num1 = (page-1)
    num2 = page
    stu = Student.stuObj2.all()[num1*3:num2*3]
    return HttpResponse(stu.values())

def stuserach(req):
    # stulist = Student.stuObj2.filter(sage__exact=18)
    # stulist = Student.stuObj2.filter(sname__contains="刘")
    # stulist = Student.stuObj2.filter(sname__startswith="张")
    # stulist = Student.stuObj2.filter(sname__endswith="1")
    # stulist = Student.stuObj2.filter(sname__isnull=False)
    # stulist = Student.stuObj2.filter(pk__in=[1,4])
    # stulist = Student.stuObj2.filter(sage__lt=30)
    # stulist = Student.stuObj2.filter(createTime__year=2018)
    # stulist = Student.stuObj2.filter(sname__contains="刘%")
    #查找描述中含有刘德华三个字的学生属于哪个班级 123
    # grade = Grades.objects.filter(student__scontend__contains="刘德华")

    # from django.db.models import Max
    # stu_MaxAge = Student.stuObj2.aggregate(Max('sage'))
    from django.db.models import F,Q
    # grade = Grades.objects.filter(ggirlnum__gt=F('gboynum'))
    # s = Student.stuObj2.filter(Q(sage__gt=30) | Q(sage__lt=19))
    # s = Student.stuObj2.filter(Q(sage=34))
    s = Student.stuObj2.filter(~Q(sage__gt=34))
    return HttpResponse(s.values())