# ！usr/bin/eny python3
# _*_ encoding=utf-8 _*_
'''
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax+n
    return ax
print(calc_sum(1,3,4))
'''
from os import name

'''
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
            return ax
    return sum
'''

'''
# ! usr/bin/eny python3
# _*_ coding=utf-8 _*_

import functools
def log1(text1):
    def dec1(func):
        @functools.wraps(func)
        def wrapper1(*args, **kw):
            print('log1:启动 %s %s()函数:' % (text1, func.__name__))
            print('log2:结束 %s %s()函数:' % (text1, func.__name__))
            return func(*args, **kw)
        return wrapper1
    return dec1

def log2(text2):
    def dec2(func):
        @functools.wraps(func)
        def wrapper2(*args, **kw):
            print('log2:启动 %s %s()函数:' % (text2, func.__name__))
            print('log2:结束 %s %s()函数:' % (text2, func.__name__))
            return func(*args, **kw)
        return wrapper2
    return dec2

@log2('我是log2')
@log1('我是log1')

def now():
    print("20180721")

print(now())
k=now.__name__
print(k)
'''
'''
# ! usr/bin/eny python3
# _*_ coding=utf-8_*_

class Student(object):
    def __init__(self,name,score,gender):
        self.__name=name
        self.__score=score
        self.__gender=gender
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def get_gender(self):
        return self.__gender

    def set_name(self,name):
        self.__name=name
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__name = score
        else:
            raise ValueError('bad score')
    def set_gender(self,gender):
        if gender == '男' or '女':
            self.__gender=gender
        else:
            raise ValueError('错误性别')
    def print_score(self):
        print(self.__score)
    def get_score_dengji(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'

allen=Student('allen',100,'男')


def test_get_name():
    if allen.get_name()=='allen':
        print('test_get_name测试通过')
    else:
        print('test_get_name测试不通过')

def test_get_score():
    if allen.get_score()==100:
        print('test_get_score测试通过')
    else:
        print('test_get_score测试不通过')


def test_get_gender():
    if allen.get_gender()=='男':
        print('test_get_gender测试通过')
    else:
        print('test_get_gender测试不通过')

def test_set_name():
    if allen.set_name(mark)=='mark':
        print('test_set_name测试通过')
    else:
        print('test_set_name测试不通过')
'''
'''
print(test_get_name())
print(test_get_score())
print(test_get_gender())
print(test_set_name())
'''
'''

s1=input('请输入你的姓名:')
s2=int(input('请输入你的分数:'))
s3=input('请输入你的性别:')
Mark=Student(s1,s2,s3)
print(Mark.get_score())
print(Mark._Student__name)
print(Mark.get_gender())
Mark.set_gender('女')
print(Mark.get_gender())

'''

'''
# ！ usr/bin/eny python3
# _*_ coding=utf-8_*_
class Student(object):
    __slots__=('name','age')

s=Student()

s.name='Mark'
s.age='27'


print(s.name)
print(s.age)
'''
'''
class Student(object):
    def get_score(self):
        return self.score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an interger!')
        if value < 0 or value > 100:
            raise ValueError('score must be between 0~100')
        self._score=value
s=Student()
s.set_score(60)
s.get_score()
s.set_score(9999)
'''
'''
装饰器用于管理和增强函数和类行为的代码
提供一种在函数或类定义中插入自动运行代码的机制：
日志，测试，跟踪
'''


'''
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
#print(add(3,5))
#print(subtract(5,3))
def action(x,y,func):
    return func(x,y)

print(action(5,2,add))
print(action(5,2,subtract))
print(action(5,2,lambda x,y:x*y))


'''




# ! usr/bin/eny python3
# _*_ coding=utf-8 _*_
# __author__="Created by Mark at 2018.07.22"
# __copyright__='Copyright 2018,Mark'

'''
def greeting():
    def hello():
        return "Hello"
    return hello
print(greeting()())

'''
'''
def func_1():
    x=10
    def func_2():
        nonlocal x
        return x+10
    return func_2()
print(func_1())
'''
'''
def p_decorator(func) -> object:
    def wrapper(*args,**kwargs):
        return '<p>' + func(*args,**kwargs) + '</p>'
    return wrapper

# @p_decorator
def get_text():
    return '欢迎学习Python'

if __name__=='__main__':
    html=p_decorator(get_text)
    print(html())

'''
'''
# ! usr/bin/eny python3
# _*_ coding=utf-8 _*_
__author__="Mark"
__copyright__='Mark'

class P(object):
    def __init__(self,func):
        self.func=func

    def __call__(self, *args, **kwargs):
        return '<p>'+ self.func(*args,**kwargs) + '</p>'

@P
def get_text():
    return '欢迎学习优品课程课程'

def get_upper_text(text):
    return text.upper()


if __name__=='__main__':
    pass
   # p=P(get_upper_text)('mark')
  #  print(p)


'''



# ! usr/bin/eny python3
# _*_ coding=utf-8 _*_
__author__='Mark'
__copyright__='Mark'

def decorator(func):
    def wrapper(*args,**kwargs):
        print('Mark在学习Python的知识，想成为Python大神')
        return func(*args,**kwargs)
    return wrapper

@decorator
def Hello(x,y):
    print(x+y,x*y)

class Student(object):
    __slots__=('name','gender')
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

    @decorator
    def get_name(self):
        return self.name

if __name__=='__main__':
    print(Hello(2,3))
    print(Student('Mark','男').get_name())
































































