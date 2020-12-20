from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
"""stusys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.db import transaction
from django.urls import path

from stusys.inouttake import inout
from stusys.score import score
from stusys.student import student

"""Django01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.shortcuts import HttpResponse
import pymysql

#登录页面
def login(request):
    #指定要访问的页面，render的功能：讲请求的页面结果提交给客户端
    return render(request,'login.html')
#注册页面
def regiter(request):
    return render(request,'regiter.html')
#定义一个函数，用来保存注册的数据
def addstu(request):
    return render(request,'addstu.html')

def altstu(request):
    return render(request,'altstu.html')

def selstu(request):
    return render(request,'selstu.html')
def index(request):
    return render(request,'index.html')
def delstu(request):
    return render(request,'delstu.html')
def selsc(request):
    return render(request,'selsc.html')
def score_insert(request):
    return render(request,'inssc.html')
def score_update(request):
    return render(request,'upsc.html')

def save(request):
    has_regiter = 0#用来记录当前账号是否已存在，0：不存在 1：已存在
    a = request.GET#获取get()请求
    #print(a)
    #通过get()请求获取前段提交的数据
    userName = a.get('username')
    passWord = a.get('password')
    #print(userName,passWord)
    #连接数据库
    db = pymysql.connect(host = 'localhost',
                         user = 'root',
                         password = 'root'
                         )
    #创建游标
    cursor = db.cursor()
    #SQL语句
    cursor.execute('use stusys')
    sql1 = 'select * from user1'
    #执行SQL语句
    cursor.execute(sql1)
    #查询到所有的数据存储到all_users中
    all_users = cursor.fetchall()
    i = 0
    while i < len(all_users):
        if userName in all_users[i]:
            ##表示该账号已经存在
            has_regiter = 1

        i += 1
    if has_regiter == 0:
        # 将用户名与密码插入到数据库中
        sql2 = 'insert into user1(username,password) values(%s,%s)'
        cursor.execute(sql2,(userName,passWord))
        db.commit()
        cursor.close()
        db.close()
        return HttpResponse('注册成功')
    else:

        cursor.close()
        db.close()
        return HttpResponse('该账号已存在')

def query(request):
    a = request.GET
    userName = a.get('username')
    passWord = a.get('password')
    user_tup = (userName,passWord)
    db = pymysql.connect(host = 'localhost',
                         user = 'root',
                         password = 'root',
                         )
    cursor = db.cursor()
    cursor.execute('use stusys')
    sql = 'select username,password from user1'
    cursor.execute(sql)
    all_users = cursor.fetchall()
    cursor.close()
    db.close()
    has_user = 0
    i = 0
    while i < len(all_users):
        if user_tup == all_users[i]:
            has_user = 1
        i += 1
    if has_user == 1:
        return render(request,'index.html')
    else:
        return HttpResponse('用户名或密码有误')


#数据库操作


# def stu_insert(request):
#     a = request.GET  # 获取get()请求
#     # print(a)
#     # 通过get()请求获取前段提交的数据
#     stu_ID = a.get('stu_id')
#     stu_Name = a.get('stu_name')
#     stu_Sex = a.get('stu_sex')
#     stu_Age = a.get('stu_age')
#     stu_Num = a.get('stu_num')
#     # 连接数据库
#     db = pymysql.connect(host='localhost',
#                          user='root',
#                          password='root'
#                          )
#     # 创建游标
#     cursor = db.cursor()
#     # SQL语句
#     cursor.execute('use stusys')
#     # 将用户名与密码插入到数据库中
#     sql2 = 'insert into stu(stu_id ,stu_name ,stu_sex ,stu_age,stu_num) values(%s,%s,%s,%s,%s)'
#     cursor.execute(sql2, (stu_ID, stu_Name ,stu_Sex ,stu_Age,stu_Num))
#     db.commit()
#     cursor.close()
#     db.close()
#     return render(request,'index.html')#转到首页

# def stu_sel(request):
#     a = request.GET
#     stu_ID = a.get('stu_id')
#     db = pymysql.connect(host="localhost", user="root", passwd="root", db="stusys", port=3306)
#     cursor = db.cursor(pymysql.cursors.DictCursor)
#     sql = "select * from stu where stu_id ='%s';"%stu_ID
#     cursor.execute(sql)
#
#     if cursor.rowcount == 0:
#         return HttpResponse("不存在该学生信息")
#     else:
#         c = cursor.fetchall()
#         print(c)
#         return render(request,'selstu.html',{'c':c})
#
#
# def stu_update(request):
#     a = request.GET
#     stu_ID = a.get('stu_id')
#     stu_Name = a.get('clas_name')
#     stu_Sex = a.get('stu_sex')
#     stu_Age = a.get('stu_age')
#     stu_Num = a.get('stu_num')
#     db = pymysql.connect(host="localhost", user="root", passwd="root", db="stusys", port=3306)
#     cursor = db.cursor()
#     sql1 = "update stu set stu_name='%s' WHERE stu_id='%s'" % (stu_Name,stu_ID)
#     cursor.execute(sql1)
#     sql2 = "update stu set stu_sex='%s' WHERE stu_id='%s'" % (stu_Sex, stu_ID)
#     cursor.execute(sql2)
#     sql3 = "update stu set stu_age='%s' WHERE stu_id='%s'" % (stu_Age, stu_ID)
#     cursor.execute(sql3)
#     sql4 = "update stu set stu_num='%s' WHERE stu_id='%s'" % (stu_Num, stu_ID)
#     cursor.execute(sql4)
#     db.commit()
#     db.close()
#     return HttpResponse('suessfully')
#
# def stu_del(request):
#     a = request.GET
#     stu_ID = a.get('stu_id')
#     db = pymysql.connect(host="localhost", user="root", passwd="root", db="stusys", port=3306)
#     cursor = db.cursor()
#     sql = "delete from stu where stu_id = '%s'"% stu_ID
#     cursor.execute(sql)
#     db.commit()
#     db.close()
#     return render(request,'index.html')




urlpatterns = [
    path('admin/', admin.site.urls),#系统默认创建的
    path('',login),#用于打开登录页面
    path('index/',index),
    path('regiter/',regiter),#用于打开注册页面
    path('regiter/save',save),#输入用户名密码后交给后台save函数处理
    path('query',query),#输入用户名密码后交给后台query函数处理
    path('addstu/',addstu),#向数据库添加学生数据
    path('stu_insert',student.stu_insert),#向数据库添加学生数据
    path('addstu/stu_insert',student.stu_insert),
    path('addstu/index',index),
    path('altstu',altstu),#修改数据库学生数据
    path('stu_update',student.stu_update),
    path('stu_update/index',index),
    path('selstu',selstu),#查询学生数据pl
    path('stu_sel',student.stu_sel),
    path('stu_sel/index',index),
    path('delstu',delstu),
    path('del_stu',student.stu_del),
    path('del_stu/index',index),
    path('uploadFile',inout.upload_file),#上传文件路由
    path('score_sel',selsc),#成绩管理系统
    path('score_sel1',score.score_sel),#跳转到查询成绩
    path('score_insert',score_insert),#跳转到成绩添加页面
    path('score_insert1',score.score_insert),#调用课程添加函数
    path('score_update',score_update),#切换到成绩更改页面
    path('sc_update',score.score_update),#调用成绩更改函数


]
urlpatterns += staticfiles_urlpatterns()
