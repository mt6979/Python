from django.shortcuts import render
from .models import Student,Grades

# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse("This is the mainpage of myApp!!!")
    username = request.session.get("name","游客")
    return render(request,'myApp/myAppindex.html',{'username':username})

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

def attributes(req):
    print(req.path)
    print(req.method)
    print(req.encoding)
    print(req.GET)
    print(req.POST)
    print(req.FILES)
    print(req.COOKIES)
    print(req.session)
    return HttpResponse("OOOOO")
#http://127.0.0.1:8080/myApp/get1?a=565&b=%E5%88%98%E8%A1%8D%E8%81%AA
def get1(req):
    a = req.GET.get("a")
    b = req.GET.get("b")
    return HttpResponse("a = "+a+"  b = "+b)
#django2 中不允许通过GET传递多个相同拥有相同键的值，后面的键的值会覆盖前面的键的值
#djagn
def get2(req):
    a = req.GET.get("a")
    a1 = a[0]
    a2 = a[1]
    b = req.GET.get("b")
    return HttpResponse("a1 = "+a1+" a2 = "+a2+" b = "+b)

def regist(req):
    if req.method == "GET":
        return render(req,"myApp/regist.html")
    else:
        name = req.POST.get("name")
        age = req.POST.get("age")

        return HttpResponse("你好！！"+name+"  "+age)

def cookietest(req):
    res = HttpResponse()
    # cookie = req.COOKIES
    # res.set_cookie("lyc","good")
    # res.write("<h1>"++"</h1>")
    return res
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def redirect1(req):
    return redirect("/myApp/redirect2")

def redirect2(req):
    return HttpResponse("<h1>我是重定向的页面</h1>")

def me(req):
    username = req.session.get("name",'游客')
    return render(req,'myApp/me.html',{'username':username})
def submit(req):
    username = req.POST.get("name")
    req.session['name'] = username#不设置两个星期后过期
    req.session.set_expiry(10)#10s之后过期
    return redirect('/myApp/main')
def main(req):
    username = req.session.get("name","游客")
    return HttpResponse("<h1>"+username+"</h1>")
from django.contrib.auth import logout
def quit(req):
    # req.session['name'] = None
    logout(req)
    req.session.clear()
    req.session.flush()
    return HttpResponse('<h1 style="color: red">您已经成功退出了。。</h1>')