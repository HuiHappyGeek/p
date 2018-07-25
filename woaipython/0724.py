# ！usr/bin/python eny
# _*_ coding=utf-8 _*_
__author__ = 'Mark'
__copyright__ = 'Mark'
'''
from time import sleep
from multiprocessing import Process
import os

def run(str):
    while True:
        print('子进程：coco is a %s man--%s--%s' % (str,os.getpid(),os.getppid()))
        sleep(1.2)

if __name__ == '__main__':
    print('父进程启动--%s' % os.getpid())
    p=Process(target=run,args=('nice',))
    p.start()
    while True:
        print('父进程：mark is a good man--%s' % os.getpid())
        sleep(1)

        # 不会执行run方法，只有上面的while循环结束才可以执行
    run()
'''


