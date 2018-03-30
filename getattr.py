# coding=utf-8
# 面试题：用魔法方法实现打印相应内容


class Foo(object):

    def __init__(self):
        pass

    def __getattr__(self, item):
        print (item),
        return self

    def __str__(self):
        return ""


print(Foo().think.different.ocean.python)
