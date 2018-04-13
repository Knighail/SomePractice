# coding=utf-8

from mysql_encap import MysqlEncap

#id = raw_input("请输入要修改的用户id")
#name = raw_input("请输入用户名")

# sql_insert = 'update students set name=%s where id=%s'
sql_select = 'select * from students'
# params=[name,id]

test = MysqlEncap('localhost',3306,'root','413413','test')
# test.iud(sql,params)
result = test.select(sql_select)
print result