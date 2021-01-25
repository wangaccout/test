# 求和
# num1 = input('请输入第一个数字')
# num2 = input('请输入第二个数字')
# sum1 = num1 + num2
# sum2 = float(num1) + float(num2)
# print(sum1)
# print(sum2)
# print('数字{0}和{1}相加结果为：{2}'.format(num1, num2, sum2))

# print('两数之和为%.2f' % (float(input('请输入第一个数字')) + float(input('请输入第二个数字'))))

# 平方根
# import cmath  # 复数数学模块
# num = float(input('请输入一个数字：'))
# # num_sqrt = num ** 0.5  # 适用于正数
# # print('%.1f的平方根为%.1f' % (num, num_sqrt))
# num_sqrt = cmath.sqrt(num)  # 实数和复数
# print('{0}的平方根为{1:.2f}+{2:.2f}j'.format(num, num_sqrt.real, num_sqrt.imag))


# def sqrt():
#     # import cmath
#     # # 计算实数和复数平方根# # 导入复数数学模块 isinstance(num ,  (float,int) )
#     num = input('输入第一个数字：')
#     if num.__contains__('-') and num.__contains__('.'):  # 负数、浮点数
#         num_sqrt = cmath.sqrt(float(num))
#         print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(float(num), num_sqrt.real, num_sqrt.imag))
#     elif num.__contains__('-'):  # # 负数、整数
#         num_sqrt = cmath.sqrt(int(num))
#         print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(int(num), num_sqrt.real, num_sqrt.imag))
#     else:
#         if num.__contains__('.'):  # 非负数、浮点数 整数
#             num_sqrt = float(num) ** 0.5
#             print(' %0.3f 的平方根为 %0.3f' % (float(num), num_sqrt))
#         else:  # # 非负数、整数
#             num_sqrt = int(num) ** 0.5
#             print(' %0.3f 的平方根为 %0.3f' % (int(num), num_sqrt))
#
# sqrt()

# 三角形面积
# import math
# import unicodedata
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#     try:
#         unicodedata.digit(s)  # 把一个合法的数字字符串转换为数字值
#         return True
#     except (TypeError, ValueError):
#         pass
#     return False
# def calculate(a, b, c):
#     if is_number(a) and is_number(b) and is_number(c):
#         a = float(a)
#         b = float(b)
#         c = float(c)
#         if a > 0 and b > 0 and c > 0:
#             while a+b<=c or a+c<=b or b+c<=a:
#                 print('输入的边长无法构成三角形')
#                 a = float(input('请输入边长a:'))
#                 b = float(input('请输入边长b:'))
#                 c = float(input('请输入边长c:'))
#                 # calculate(a, b, c)  # 此方法是否调用？？？？
#             p = (a+b+c) / 2
#             area = math.sqrt(p*((p-a)*(p-b)*(p-c)))
#             print('三角形的面积是：%.2f' % area)
#         else:
#             print('三角形的边长必须大于0，请输入大于0的数')
#     else:
#         print('请输入数字类型')
# a = input('请输入边长a')
# b = input('请输入边长b')
# c = input('请输入边长c')
# calculate(a, b, c)

# 计算圆的面积
# import math
# pi = math.pi
# def area():
#     r = input('请输入半径：')
#     while r.isdigit() == False or float(r) <= 0:
#         print('请输入大于0的数字')
#         r = input('输入半径：')
#     else:
#         r = float(r)
#         area = pi * (r * r)
#         print('圆的面积是：%0.2f' % area)
#         print(pi)
# area()

# 随机数
# import random
# print(random.randint(1, 10))  # 1到10的随机整数
# print(random.random())  # 0到1的随机浮点数
# print(random.uniform(1.1, 5.4))  # 1.1到5.4的随机浮点数
# print(random.choice(' '))  # 从序列中随机选取一个元素
# print(random.randrange(1, 100, 2))  # 1到100间隔为2的随机整数

# 变量交换
# x = input('请输入X:')
# y = input('请输入Y:')
# x, y = y, x
# # temp = x
# # x = y
# # y = temp
# print('交换后的X值为：', x)
# print('交换后的Y值为：{}'.format(y))

# 判断字符串是否为数字
# def is_number(s):
#     try:  # 如果能运行float(s)语句，返回True(字符串s是浮点数)
#         float(s)
#         return True
#     except ValueError:  # ValueError为Python的一种标准异常，表示‘传入无效的参数’
#         pass  # pass不做任何事情，一般用做占位语句
#     try:
#         import unicodedata  # 处理ASCii码的包
#         # for i in s:
#         # isdigit() 方法检测字符串是否只由数字组成
#         # isnumeric()方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
#         unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
#         return True
#     except(TypeError, ValueError):
#         pass
#     return False
# print(is_number('oo'))
# print(is_number('1'))
# print(is_number('哈大家都还记得滑放假放假加防腐剂动的'))
# # 阿拉伯语 5
# print(is_number('٥'))  # True
# # 泰语 2
# print(is_number('๒'))

# 判断奇偶数
# while True:
#     try:
#         num = int(input('请输入一个数：'))
#     except ValueError:  # 不是纯数字需要重新输入
#         print('输入的不是整数')
#         continue
#     if num % 2 == 0:
#         print(num, '是偶数')
#     else:
#         print(num, '是奇数')
#     break

# 判断闰年
# year = int(input('请输入年份：'))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('{0}是闰年'.format(year))
# else:
#     print('{0}不是闰年'.format(year))

# calendar库中已经封装好了一个方法isleap()来实现判断是否为闰年
# import calendar
# year = int(input('请输入年份：'))
# cheak_year = calendar.isleap(year)
# if cheak_year == True:
#     print('闰年')
# else:
#     print('平年')










