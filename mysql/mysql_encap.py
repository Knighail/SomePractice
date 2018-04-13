# coding=utf-8

from MySQLdb import *

class MysqlEncap(object):
    """"""
    def __init__(self,host,port,user,passwd,db,charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset

    def connect(self):
        self.conn = connect(host=self.host, port=self.port, user=self.user,\
                            passwd=self.passwd, db=self.db, charset=self.charset)
        self.curs = self.conn.cursor()

    def close(self):
        self.curs.close()
        self.conn.close()

    def iud(self, sql, params):
        try:
            self.connect()

            self.curs.execute(sql,params)
            self.conn.commit()
            print ("operation complete")

            self.close()
        except Exception,e:
            print e.message

    def select(self,sql,params=[]):
        try:
            self.connect()

            self.curs.execute(sql, params)
            result = self.curs.fetchall()

            self.close()
            return result
        except Exception, e:
            print e.message

