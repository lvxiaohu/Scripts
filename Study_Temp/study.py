# -*- coding: utf-8 -*-

#打印1-100 包含4的整数：

# n=0
# while n <= 100:
#     n += 1
#     if n % 10 ==4 or n // 10 == 4:
#         pass
#     else:
#         print n
#def

# def power(x,y):
#     s = 1
#     while y >0 :
#         y -= 1
#         s *= x
#         print y
#         print s
#     print s
# power(2,3)

#递归函数
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# print fact(3)
# print 2*fact(3)

#
#
# n=0
# results=[]
# def tringles(n):
#     while n <= 10:
#         results.append(n)
#         n=n+1
#         print results
# print tringles(10)


#
# 变成杨辉三角先确定流程：
# 1.前两项无规律
#   所以先付初值
# 2.第n项起(n>=3)：
#   第一和第n个数为1
#   其余项第i项为前一行第i-1和第i个数的和
#
# 所以威力便于理解，建立了两个列表
# 其中L=list(S)为把解出的列表赋值给上一行的列表
# L=S是同一个列表会产生计算错误
#


# import time, functools
#
# def metric(fn):
#     @functools.wraps(func)
#     #print('%s executed in %s ms' % (fn.__name__, 10.24))
#
#     def wrapper(**args,**kw):
#         print('%s' % (time.ctime()))
#     return metric()
# @metric
# def fast(x,y):
#     return x+y
# print fast(2,4)

# print time.ctime()


# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(args,**kw):
#         print('%s executed in %s ms'%(fn.name,10.24))
#         return fn(args,**kw)
#     return wrapper
#
# @metric
# def fast(x,y):
#     return x+y
# print fast(2,4)

#
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
# lisa = Student('Lisa',90)
# bart = Student('Bart',59)
# print (lisa.name ,lisa.get_grade())
# print (bart.name,bart.get_grade())
#
# class Telephone_number(object):
#     class_name="hello"
#     def __init__(self,name,number):
#         self.__name=name
#         self.__number=number
#     def print_number(self):
#         print('s%' %(self.__name,self.__name))
#     def get_number(self):
#         return self.__name
#     def set_number(self):
#         self.__number=number
#
# name1 = Telephone_number('lxh',1234)
# name2 = Telephone_number('ooad',4545)
# # print(name1.class_name)
# print name1.get_number()
# print name2.number
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.__name = name
#         self.__gender = gender
#     def get_gender(self):
#         return self.__gender
#     def set_gender(self,gender):
#         self.__gender=gender
# bart = Student('Bart', 'male')
# print bart.get_gender()
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')
# print '***' * 10


# class Animal(object):
#     def run(self):
#         print('Animal is running...')
# class Dog(Animal):
#     def run(self):
#         print ('Dog is running...')
# class Cat(Animal):
#     def ok(self):
#         print('Cat is running...')
# dog=Dog()
# cat=Cat()
# dog.run()
# cat.ok()
# def run_twice(animal):
#     animal.run()
#     animal.run()
# class Tortoise(Animal):
#     def run(self):
#         print('Tortoise is running slowly...')
# run_twice(Tortoise())
#
#
# print '***' * 10

# class Student(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Student.count+=1
#
# print Student.count
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')

# class Student(object):
#     pass
# s=Student()
# s.name = 'lxh' #动态给实例绑定一个属性
# print(s.name)
#
# def set_age(self,age):
#     self.age=age
# from types import MethodType
# s.set_age=MethodType(set_age,s)
# s.set_age(11)
# s.age
#
#多线程
from multiprocessing import process
# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')
# import  re
# f=open('F:/py/filet/word.txt','r')
# IP_num=0
# php_num=0
# for i in f.readlines():
#     if re.match(r'220.178.45.242*',str(i)):
#         IP_num += 1
#         # print i
# for i in f.readlines():
#     # if re.match(r'*1.php*',str(i)):
#     #   a = re.split(r'[\s\,]+',str(i))
#     #   if  re.match(r'\s+php$',i):
#     if re.match(r'.*php', i):
#           php_num += 1
# print(IP_num)
# print(php_num)
#
# from PIL import  Image
# im = Image.open('F:/py/filet/test.jpg')
# w,h=im.



from IPy import IP
ip = IP('192.168.1.1')
print(ip.iptype())
print(ip.make_net('255.255.255.0'))
print('192.168.1.1' in IP('192.168.1.0/24'))
print(ip.reverseName())