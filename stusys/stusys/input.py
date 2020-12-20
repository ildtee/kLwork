


class input:
    #导出
    # @wapper
    # @app.route('/exportdata',methods=['GET','post'],endpoint='exportdata')
    def exportdata():
        engine = create_engine('mysql+pymysql://root:root/mybase01?charset=utf8')
        sql_query = 'select * from course;'
        df = pd.read_sql_query(sql_query, engine)
        print(df)
        df.to_excel("F:/python/project_2/static/file/db.xlsx",index=False)
        #print(df)
        #df.to_excel("F:/python/project_2/db.xlsx", index=False)
        return send_from_directory("F:/python/project_2/static/file/", filename="db.xlsx", as_attachment=True)




    #导入页面
    # @wapper
    # @app.route('/importdatapage',endpoint='importdatapage')
    # def importdatapage():
    #     return render_template("/importdatapage.html")

    #导入
    # @wapper
    # @app.route('/importdata',methods=["get","post"],endpoint='importdata')
    def importdata():
        f = request.files['excel']
        f.save(os.path.join(os.path.join(os.getcwd(), "static/file"), f.filename))
        file = os.path.join(os.path.join(os.path.join(os.getcwd(), "static/file"), f.filename))
        print(file)
        engine = create_engine('mysql+pymysql://root:root/mybase01?charset=utf8')
        df =pd.read_excel(file)

        # print(df)
        #测试表
        #pd.io.sql.to_sql(df,'course_c', engine, schema='mybase01', if_exists='append',index=False)
        pd.io.sql.to_sql(df, 'course', engine, schema='mybase01', if_exists='append', index=False)
        return redirect("/index")
