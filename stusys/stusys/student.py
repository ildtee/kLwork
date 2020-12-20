import pymysql
from django.http import HttpResponse
from django.shortcuts import render


class student:
    def stu_insert(request):
        a = request.GET  # 获取get()请求
        # print(a)
        # 通过get()请求获取前段提交的数据
        stu_ID = a.get('stu_id')
        stu_Name = a.get('stu_name')
        stu_Sex = a.get('stu_sex')
        stu_Age = a.get('stu_age')
        stu_Num = a.get('stu_num')
        # 连接数据库
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='root'
                             )
        # 创建游标
        cursor = db.cursor()
        # SQL语句
        cursor.execute('use stusys')
        # 将用户名与密码插入到数据库中
        sql2 = 'insert into stu(stu_id ,stu_name ,stu_sex ,stu_age,stu_num) values(%s,%s,%s,%s,%s)'
        cursor.execute(sql2, (stu_ID, stu_Name ,stu_Sex ,stu_Age,stu_Num))
        db.commit()
        cursor.close()
        db.close()
        return render(request,'index.html')#转到首页

    def stu_sel(request):
        a = request.GET
        stu_ID = a.get('stu_id')
        db = pymysql.connect(host="localhost", user="root", passwd="root", db="stusys", port=3306)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = "select * from stu where stu_id ='%s';" % stu_ID
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return HttpResponse("不存在该学生信息")
        else:
            c = cursor.fetchall()
            print(c)
            return render(request, 'selstu.html', {'c': c})

    def stu_update(request):
        a = request.GET
        stu_ID = a.get('stu_id')
        stu_Name = a.get('clas_name')
        stu_Sex = a.get('stu_sex')
        stu_Age = a.get('stu_age')
        stu_Num = a.get('stu_num')
        db = pymysql.connect(host="localhost", user="root", passwd="root", db="stusys", port=3306)
        cursor = db.cursor()
        sql1 = "update stu set stu_name='%s' WHERE stu_id='%s'" % (stu_Name, stu_ID)
        cursor.execute(sql1)
        sql2 = "update stu set stu_sex='%s' WHERE stu_id='%s'" % (stu_Sex, stu_ID)
        cursor.execute(sql2)
        sql3 = "update stu set stu_age='%s' WHERE stu_id='%s'" % (stu_Age, stu_ID)
        cursor.execute(sql3)
        sql4 = "update stu set stu_num='%s' WHERE stu_id='%s'" % (stu_Num, stu_ID)
        cursor.execute(sql4)
        db.commit()
        db.close()
        return HttpResponse('suessfully')

    def stu_del(request):
        a = request.GET
        stu_ID = a.get('stu_id')
        db = pymysql.connect(host="localhost", user="root", passwd="root", db="stusys", port=3306)
        cursor = db.cursor()
        sql = "delete from stu where stu_id = '%s'" % stu_ID
        cursor.execute(sql)
        db.commit()
        db.close()
        return render(request, 'index.html')
