from django.urls import path,include
from django.conf.urls import url
from .import views
urlpatterns = [

    path('',views.index),
    path('news',views.news),
    path('addStudent',views.addStudent),
    path('addStudent2', views.addStudent2),
    path('getStudents',views.getStudents),
    path('students0',views.students0),
    # path('stu/(\d+)',views.stupage),
    url(r'^stu/(\d+)/$',views.stupage),
    path('stusearch',views.stuserach),
]
