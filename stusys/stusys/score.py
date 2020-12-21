import pymysql
from django.http import HttpResponse
from django.shortcuts import render


class score:
    def score_insert(request):
        a = request.GET  # 获取get()请求
        # print(a)
        # 通过get()请求获取前段提交的数据
        stu_ID = a.get('stu_id')
        clas_ID = a.get('clas_id')
        stu_CLAS = a.get('stu_clas')
        stu_SCORE = a.get('stu_score')
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
        sql2 = "insert into score(stu_id ,clas_id ,stu_clas ,stu_score) values(%s,%s,'%s',%s)"%(stu_ID,clas_ID,stu_CLAS,stu_SCORE)
        cursor.execute(sql2)
        db.commit()
        cursor.close()
        db.close()
        return render(request,'selsc.html')#转到首页

    def score_sel(request):
        a = request.GET
        stu_ID = a.get('stu_id')
        db = pymysql.connect(host="localhost", user="root", passwd="root", db="stusys", port=3306)
        cursor = db.cursor()
        sql = "select stu_clas,stu_score from score where stu_id='%s';" %stu_ID
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return HttpResponse("不存在该学生信息")
        else:
            c = cursor.fetchall()
            c = list(c)
            print(c)
            return render(request, 'selsc.html', {'c': c})


    def score_update(request):
        a = request.GET
        stu_ID =  a.get('stu_id')
        clas_ID = a.get('clas_id')
        stu_CLAS = a.get('stu_clas')
        stu_SCORE = a.get('stu_score')
        db = pymysql.connect(host="localhost", user="root", passwd="root", db="stusys", port=3306)
        cursor = db.cursor()
        sql1 = "update score set clas_id='%s' WHERE stu_id=%s" % (clas_ID,stu_ID)
        cursor.execute(sql1)
        sql2 = "update score set stu_clas='%s' WHERE stu_id=%s" % (stu_CLAS, stu_ID)
        cursor.execute(sql2)
        sql2 = "update score set stu_score='%s' WHERE stu_id=%s" % (stu_SCORE, stu_ID)
        cursor.execute(sql2)
        db.commit()
        db.close()
        return HttpResponse('suessfully')
