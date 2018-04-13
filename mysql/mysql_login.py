# coding=utf-8

from mysql_encap import MysqlEncap

from hashlib import sha1

# 获取信息
username = raw_input("请输入用户名：")
passwd = raw_input("请输入密码：")

# 密码加密
sh = sha1()
sh.update(passwd)
passwd_sha1 = sh.hexdigest()

# 查询信息
sql = 'select passwd from userinfo where username=%s'
login = MysqlEncap('localhost',3306,'root','413413','test')
result = login.select(sql,[username])
#print result

# 验证信息
# if result is None: # 此语句成立时不存在[0][0],会报错
if len(result) ==0:
    print ("用户名不存在")
elif result[0][0] == passwd_sha1:
    print ("登录成功")
else:
    print ("密码错误")

