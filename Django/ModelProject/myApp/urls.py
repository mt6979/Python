from django.urls import path,include
from django.conf.urls import url
from .import views
urlpatterns = [

    path('',views.index),
    path('news/',views.news),
    path('addStudent/',views.addStudent),
    path('addStudent2/', views.addStudent2),
    path('getStudents/',views.getStudents),
    path('students0/',views.students0),
    # path('stu/(\d+)',views.stupage),
    url(r'^stu/(\d+)/$',views.stupage),
    path('stusearch/',views.stuserach),
    url(r'^attributes/$',views.attributes),
    url(r'^get1/$',views.get1),
    url(r'^get2/$',views.get2),
    url(r'^regist/$',views.regist),
    url(r'^cookietest/$',views.cookietest),
    url(r'^redirect1/$',views.redirect1),
    url(r'^redirect2/$',views.redirect2),
    url(r'^me/$',views.me),
    url(r'^submit/$',views.submit),
    url(r'^main/$',views.main),
    url(r'^quit/$',views.quit),


]
