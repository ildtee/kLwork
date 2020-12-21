import os
from datetime import datetime

import xlrd as xlrd
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import pymysql
from django.http import HttpResponse
from django.shortcuts import render
from xlrd import xldate_as_datetime
from django.http import HttpResponse
from xlwt import *
from io import StringIO  # 需要stringIO，这是python2中的，如果是python3，使用 from io import StringIO


def wrdb(filename):
    # 打开上传 excel 表格
    readboot = xlrd.open_workbook("D:\\upload\stu.xlsx")
    sheet = readboot.sheet_by_index(0)
    # 获取excel的行和列
    nrows = sheet.nrows
    ncols = sheet.ncols
    print(ncols, nrows)

    for i in range(1, nrows):
        row = sheet.row_values(i)
        stu_Num = row[4]
        stu_Age = row[3]
        stu_Sex = row[2]
        stu_Name = row[1]
        stu_ID = row[0]
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='root'
    )
    cursor = db.cursor()
    # SQL语句
    cursor.execute('use stusys')
    sql2 = 'insert into stu(stu_id ,stu_name ,stu_sex ,stu_age,stu_num) values(%s,%s,%s,%s,%s)'
    cursor.execute(sql2, (stu_ID, stu_Name, stu_Sex, stu_Age, stu_Num))
    db.commit()
    cursor.close()
    db.close()
    return HttpResponse('上传数据库成功了')


class inout:
    @csrf_exempt
    def upload_file(request):
        if request.method == "POST":    # 请求方法为POST时，进行处理
            myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
            if not myFile:
                return HttpResponse("no files for upload!")
            destination = open(os.path.join("D:\\upload",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作

            for chunk in myFile.chunks():      # 分块写入文件
                destination.write(chunk)
            destination.close()
            wrdb(myFile.name)
            return HttpResponse("upload over!")


    def excel_export(request):
        """
        导出excel表格
        """
        db = pymysql.connect(
            host='localhost',
            user='root',
            password='root'
        )
        cursor = db.cursor()
        # SQL语句
        cursor.execute('use stusys')
        cursor.execute('select * from stu')
        list_obj = cursor.fetchall()
        print(list_obj)
        if list_obj:
            # 创建工作薄
            ws = Workbook(encoding='utf-8')
            w = ws.add_sheet(u"数据报表第一页")
            w.write(0, 0, "id")
            w.write(0, 1, u"学生名")
            w.write(0, 2, u"stu_sex")
            w.write(0, 3, u"stu_age")
            w.write(0, 4, u"stu_num")
            # 写入数据
            excel_row = 1
            for obj in list_obj:
                stu_id = obj[0]
                stu_name = obj[1]
                stu_sex = obj[2]
                stu_age = obj[3]
                stu_num = obj[4]
                w.write(excel_row, 0, stu_id)
                w.write(excel_row, 1, stu_name)
                w.write(excel_row, 2, stu_sex)
                w.write(excel_row, 3, stu_age)
                w.write(excel_row, 4, stu_num)
                excel_row += 1
            # 检测文件是够存在
            # 方框中代码是保存本地文件使用，如不需要请删除该代码
            ###########################
            exist_file = os.path.exists("test.xls")
            if exist_file:
                os.remove(r"test.xls")
            ws.save("test.xls")
            ############################
            response = '下载成功了'
            return HttpResponse(response)
