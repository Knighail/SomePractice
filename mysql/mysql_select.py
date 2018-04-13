# coding=utf-8

from MySQLdb import *

try:
    coon = connect(host='localhost',port=3306,user='root',\
                   passwd='413413',db='test',charset='utf8')
    curs1=coon.cursor()
    sql_o = 'select * from students where id=8'
    sql_a = 'select * from students'
    curs1.execute(sql_o)
    curs1.execute(sql_a)
    result_one = curs1.fetchone()
    result_all = curs1.fetchall()
    print result_one
    print result_all
    curs1.close()
    coon.close()

except Exception,e:
    print(e.message)