from django.db import models

# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.gname
    class Meta:
        db_table ="grades"
        ordering =["id"]
# 自定义模型管理器
class StudentManager(models.Manager):
    def get_querySet(self):
        return super(StudentManager,self).get_queryset().filter(isDelete=False)
    def createStudnet(self, name, age, gender, contend, grade, lastT, createT, isD=False):
        stu = self.model()
        # print(type(grade))
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontend = contend
        stu.sgrade = grade
        stu.lastTime = lastT
        stu.createTime = createT
        return stu



class Student(models.Model):
    #自定义模型管理器
    stuObj = models.Manager()
    stuObj2 = StudentManager()
    #当自定义模型管理器，objects就不存在了
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.CharField(max_length=20)
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    #关联外键
    sgrade = models.ForeignKey("Grades",on_delete=models.CASCADE)
    def __str__(self):
        return self.sname
    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateField(auto_now_add=True)
    class Meta:
        db_table ="students"
        ordering =["id"]#升序  -id降序
    @classmethod#类方法
    def createStudent(cls,name,age,gender,content,grade,lastT,createT,isDel=False):
        stu = cls(sname=name,sage=age,sgender=gender,scontend=content,sgrade= grade,lastTime=lastT,createTime=createT,isDelete=isDel)
        return stu

