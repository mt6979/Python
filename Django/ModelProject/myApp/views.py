from django.shortcuts import render
from .models import Student,Grades
import os

# import sys
# sys.path.append('M:\PythonWeb\Django\ModelProject\ModelProject')
# import settings
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
    req.session.set_expiry(1000)#1000s之后过期
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

def s_list(req):
    s_lists = Student.stuObj2.all()
    print(s_lists)
    return render(req,'myApp/s_list.html',{'s_list':s_lists,'num':10,'hh':'<h1>这是一个h1标签</h1>'})

def good(req,id):
    return render(req,'myApp/good.html',{'num':id})

def qf(req):
    return render(req,'myApp/base.html')
def qf1(req):
    return render(req,'myApp/base1.html')

def verifycode(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), random.randrange(20, 100))
    width = 100
    height = 50
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]
    #构造字体对象
    font = ImageFont.truetype(r'D:\fonts\georgiai.ttf', 40)
    #构造字体颜色
    fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor1)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor2)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor3)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor4)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    # request.session['verifycode'] = rand_str
    #内存文件操作
    request.session['verify'] = rand_str
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

def dl(req):
    f = req.session.get('flag',True)
    s = ''
    if f == False:
        s = '，验证码输入有误，请重新输入'
    req.session['flag'] = True
    return render(req,'myApp/dl.html',{'flag':s})


def dlcheck(req):
    code1 = req.POST.get('verifycode').upper()
    code2 = req.session['verify'].upper()
    if code1 == code2:
        return HttpResponse("登录成功")
    else:
        req.session['flag'] = False
        return redirect('/myApp/dl')

def upfile(req):
    return render(req,'myApp/upfile.html')
from django.conf import settings
def savefile(req):
    if req.method == 'POST':
        f = req.FILES["img_file"]
        filepath = os.path.join(settings.MEDIA_ROOT,f.name)
        with open(filepath,'wb') as fw:
            for info in f.chunks():
                fw.write(info)
        return HttpResponse('上传成功')
    else:
        return HttpResponse('上传失败')
from .models import Student
from django.core.paginator import Paginator
def studentpage(req,pageid):
    alllist = Student.stuObj2.all()
    paginator = Paginator(alllist,2)
    page = paginator.page(pageid)
    for i in page:
        print(i.sname)
    return render(req,'myApp/student_list.html',{'student':page})





