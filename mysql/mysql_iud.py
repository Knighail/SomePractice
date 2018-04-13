# coding=utf-8

from MySQLdb import *

try:
    conn = connect(host='localhost',port=3306,user='root',\
                   passwd='413413',db='test',charset='utf8')
    curs1 = conn.cursor()

    # 增加
    # sql = 'insert into students(name) values("大米")'
    # 修改
    sql = 'update students set name="小米" where id=8'
    # 删除
    # sql = 'delete from students where id=9'
    count = curs1.execute(sql)
    print count
    conn.commit()
    print "ok"
    curs1.close()
    conn.close()
except Exception, e:
    print e.message