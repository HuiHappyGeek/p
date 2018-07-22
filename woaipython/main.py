'''
错误异常处理
错误类型：
语法错误,SyntaxError: EOL while scanning string literal
语义错误,ZeroDivisionError: division by zero   AttributeError:
逻辑错误,

'''
'''
try:
    x=5/0
    print(x)
except ZeroDivisionError as e:
    print('不能除以0',e)
except:
    print('其他错误')
else:
    print('没有异常')
'''
'''
class Person:
    def __init__(self,name):
        self.name=name
p=Person('Peter')
try:
    print(p.age)
except AttributeError as e:
    print('遇到异常属性',e)
finally:
'''
'''
f = open('/Users/Mark/Coco/p/woaipython/learning.py')
try:
    f.read()
except:
    print('文件操作遇到错误')
finally:
    f.close()
'''
'''
def method():
    raise NotImplementedError('该方法还没有开发')

print(method())
'''

'''
def get_formatted_name(first, last):
    full_name = '{} {}'.format(first, last)
    return full_name.title()
print(get_formatted_name('tom', 'lee'))

'''
class Coder(object):
    def __init__(self, name):
        self.name = name
        self.skills = []

    def mastering_skill(self, skill):
        self.skills.append(skill)

    def show_skills(self):
       # print('掌握技能：')
        for skill in self.skills:
            print('-', skill)

