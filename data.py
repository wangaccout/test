from collections import deque

# 数字,数字类型转换，运算
# a = 1.0
# print(int(a))
#
# b = (50 - 5 * 6) / 4  # 整数除法返回浮点型
# c = 50 % 4  # 返回余数
# d = 20 // 4  # 整数除法返回向下取整后的结果
# e = 7.0 // 3  # 它与分母分子的数据类型有关系
# f = 7 //3.0
# g = 5 ** 2  # 幂运算
# print(b)
# print(c)
# print(d, e, f, g)

# 字符串 运算、访问值、三引号、格式化
# string1 = 'qwertyui'
# string2 = '234567'
# string3 = string1 + string2
# string4 = string1[1: 3]
# string5 = """fhgodf\nihgig
# fdhgodfihgd"""
# print(string3)
# print(string4)
# print(string2 * 2)
# print(string5)
# print("我叫%s 今年%d岁!" % ('小明', 10))
#
# if 'g' in string1:
#     print('ok')
# else:
#     print("no")
print("\tPython")  # \t 表示空四个字符，也称缩进，相当于按一下tab键
print("\n123\n456\n789")  # \n 换行，相当于按一下回车键
print("自然数：\n\t123\n\t456\n\t789")  # \n\t 换行加每行空四格
print("\t\n123\t\n456\t\n789")  # 和\n效果一样，不建议使用
print(r'C:\Users\name')  # r 表示转义字符'\'，就是一个普通字符'\'，不表示任何意义
# print(C:\Users\name')  # 报错，\U \u 表示Unicode字符串
print('C:\Administrator\name')
print("It doesn't")


# 列表
list1 = [1, 2, 3, 4, 5, 0]
list2 = ['a', 'b', 'c', 'd']
list2[2] = 2
print(list1[1: 6])
print(list2)
# del list2[2]
list2.append(6)  # 末尾添加6
list2.insert(0, 0)  # 第0个位置插入0
list2.extend(list1)  # 将list1添加到list2中
list2.pop(0)  # 删除第0个位置的元素
list2.remove('d')  # 删除 d
# list2.popleft()
print(list2)
print(list2.index(6), list2.count(2))  # 6的索引，2的总数
list1.sort()  # 对列表中的元素进行排序
print(list1)
list1.reverse()  # 倒序排序
print(list1)
print(len(list1))
print(list1[-2])
print(list1.copy())  # 复制列表

queue = deque(["Eric", "John", "Michael"])  # 列表作为队列使用，第一个加入的元素第一个取出来
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.popleft()
print(queue)

# 元组
# tup1 = ('a', 'b', 'c', 'd')
# tup2 = (1, 2, 3)
# tup3 = tup1 + tup2
# tup4 = (20,)  # 只有一个元素时，要加 , 不加的话是数字
# tup5 = (20)
# print(tup1[1:])
# print(tup3)
# print(type(tup4), type(tup5))

# 字典
# dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print(dict1['Name'])
# del dict1['Age']
# print(dict1)
# dict1.clear()
# print(dict1)
# del dict1
# print(dict1)
# print(dict1['Name'])

# confusion = {}
# confusion[1] = 1
# confusion['1'] = 2
# confusion[1] += 1
#
# sum = 0
# for k in confusion:
#     sum += confusion[k]
# print(sum)
# print(confusion)
#
# x = True
# country_counter = {}
#
# def addone(country):
#     if country in country_counter:
#         country_counter[country] += 1
#     else:
#         country_counter[country] = 1
#
# addone('China')
# addone('Japan')
# addone('china')
# print(len(country_counter),country_counter)

# 集合#####
# set1 = set()
# set1.add('awe')
# print(set1)
# set1.update('1', 'q')
# set1.update({4, 's'})
# print(set1)
# set1.remove('1')
# print(set1)

# numbers = [1, 3, 6]
# newNumbers = tuple(map(lambda x: x , numbers))
# print(newNumbers)


