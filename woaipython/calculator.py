# ! usr/bin/eny python3
# _*_ coding=utf-8 _*_
__author__='Mark'
__copyright__='Mark'

class Calculator(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def subtract(self):
        return self.x-self.y
    def multiply(self):
        return self.x*self.y
    def divide(self):
        return self.x/self.y

if __name__=='__main__':
    c=Calculator(5,8)
    print(c.add())


