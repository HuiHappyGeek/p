
'''
a = 100 + 200 + 300;
print(a);
'''

# name=input();
'''
name=input('请输入你的名字：');
print('hello',name);
'''

# print('1024 x 768 =',1024*768);
# print absolute value of an interger
'''
a=int(input('请输入一个数：'));
if a >=0:
    print('绝对数为：',a)
else:
    print(-a)
'''


'''
# ! /usr/bin/env python3
# _*_ coding=utf-8 _*_
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('数据类型错误')
    if x>= 0:
        return x
    else:
        return -x
print(my_abs(int(input('请输入：'))))

'''

'''
# ！ usr/bin/eny python3
# _*_ coding=utf-8 _*_

def yield_test(n):
    for i iange(n):  #n rrange(5)=[0,1,2,3,4]
       # print('i=',i)
        yield call(i)  #[0,2,6,4,8]
        print("i=",i)
    #做一些其他事情
    print("do something")
    print("end")

def call(i):
    return i*2

#使用for循环
for i in yield_test(5):  #[0,2,6,4,8]
   print(i,",")
'''


'''
# ！usr/bin/eny python3
# _*_ encoding=utf-8 _*_

def fib(max):
    n,a,b=0,0,1 #n:第几个月  a:上月数量  b：本月数量
    while n < max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

for x in fib(10):
    print(x)
'''

'''
# ！ usr/bin/eny python3
# _*_ encoding=utf-8 _*_

def f(x):
    return x*x
r=map(f,range(10))
print(list(r))

'''
'''
# ！ usr/bin/eny python3
# _*_ encoding=utf-8 _*_

from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,]))
'''
'''
from functools import reduce
def fn(x,y):
    return 10*x+y
k=reduce(fn,[1,3,5,7,9])
print(k)
'''
'''
from functools import reduce

def fn(x,y):
    return 10*x+y

def char2num(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]

k=reduce(fn,map(char2num,'13579'))
print(k)
'''

'''
# ! usr/bin/eny python3
# _*_ encoding=utf-8 _*_
s1=input("请输入第1个姓名：")
s2=input("请输入第2个姓名：")
s3=input("请输入第3个姓名：")
L1=[s1,s2,s3]
def normalize(name):
    return name.capitalize()
L2=list(map(normalize,L1))
print(L2)

L3=['aLLEn','IREne','JeffChen']
L4=list(map(normalize,L3))
if L4 ==['Allen','IrEne','Jeffchen']:
    print("测试通过")
    print(L4)
else:
    print("测试不通过")

'''
'''
# ! usr/bin/eny python3
# _*_ encoding=utf-8 _*_
def is_odd(n):
    return n % 2==1
print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A',' ','B',None,'C',''])))
'''

# ! usr/bin/eny python3
# _*_encoding=utf-8_*_

def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)

for n in primes():
    if n<1000:
        print(n)
    else:
        break


