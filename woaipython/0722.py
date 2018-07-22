# ! usr/bin/eny python3
# _*_ coding=utf-8 _*_
__author__='Mark'
__copyright__='Mark'
'''
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.__score=score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError('请输入正数的分数')
        if score < 0 or score >100:
            raise ValueError('请输入0~100的分数')
        self.__score=score

s=Student('Bob',60)
print(s.score)
print(s.score)
'''
'''
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__=__str__
print(Student('Michael'))
s=Student('Michael')
print(s)
'''
# __iter__
'''
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1 #初始化两个计数器a,b
    def __iter__(self):
        return self    #实例本身就是迭代对象，故返回自已

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a >1000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)
'''
'''
class Fib(object):
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
print(Fib()[100])
'''

# __getattr__
'''
class Student(object):
    def __init__(self):
        self.name='Michael'
    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='gender':
            return '男'
        raise AttributeError('没有这个属性')
s=Student()
print(s.name)
print(s.gender)
print(s.score)
print(s.area)
'''

'''
def fn(self,name='world'):
    print('Hello,%s' % name)

Hello=type('Hello',(object,),dict(hello=fn))
h=Hello()
print(Hello().hello())
'''





















