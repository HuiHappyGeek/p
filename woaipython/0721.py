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

'''
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
            return ax
    return sum
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
