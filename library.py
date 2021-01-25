import os  # 操作系统接口
import glob  # 文件通配符
import sys  # 命令行参数
import re  # 字符串正则匹配
import math  # 为浮点运算提供了对地城C函数库的访问
import random  # 提供了生成随机数的工具
from datetime import date  # 日期和时间
import zlib  # 数据压缩
from timeit import Timer  # 性能度量
import doctest  # 测试模块，doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试
import unittest  # unittest模块不想doctests模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集
import urllib
from urllib.request import urlopen
from urllib.parse import urlencode


# print(os.getcwd())  # 返回当前的工作目录
# # print(dir(os))
# # print(help(os))
# print(glob.glob('*.py'))  # 从目录通配符搜索中生成文件列表
# print(sys.argv)  # 命令行参数
# print(re.findall(r'\bf[a-z]*', 'which foot or hang fell fastest'))
# print('tea for too'.replace('too', 'two'))
# print(math.log(1024, 2))
# print(math.cos(math.pi / 4))
# print(random.choice([1, 2, 3]))
# print(random.sample(range(100), 10))  # sampling without replacement
# print(random.random())  # random float
# print(random.randrange(5))   # random integer chosen from range(6)
# now = date.today()
# print(now)
# print(now.strftime('%m-%d-%y.%d %b %Y is a %A on the %d day of %B.'))
# birthday = date(1992, 10, 1)
# age = now - birthday
# print(age.days)
# s = b'hello hello world'
# print(len(s))
# t = zlib.compress(s)
# print(len(t))
# print(zlib.decompress(t))
# print(zlib.crc32(s))
# print(Timer('t=a; a=b; b=t', 'a=1;b=2').timeit())
# print(Timer('a,b = b,a', 'a=1;b=2').timeit())
# def average(values):
#     return sum(values) / (len(values))
# # print(average([10, 20, 30]))
# doctest.testmod()
# class TestStatisticalFunctions(unittest.TestCase):
#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         self.assertRaises(ZeroDivisionError, average, [])
#         self.assertRaises(TypeError, average, 20, 30, 70)
#
# if __name__ == '__main__':
#     unittest


url='http://www.xxx.com/login'
data={"username":"admin","password":123456}
req_data=urlencode(data)#将字典类型的请求数据转变为url编码
res=urlopen(url+'?'+req_data)#通过urlopen方法访问拼接好的url
res=res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

print(res)



