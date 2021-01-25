# while循环
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print('1到%d之和为：%d' % (counter, sum))

# var = 1
# while var == 1:  # 无限循环
#     num = int(input('输入一个数：'))
#     print('你输入的数字是：', num)
# print('ok')

# a = 1
# while a:
#     print('yes')

# count = 1
# while count < 5:  # while 循环使用 else 语句
#     print(count, '小于5')
#     count += 1
# else:
#     print(count, '大于或等于5')

# for 语句
list1 = [1, 2, 3, 4]
for li in list1:
    if li == 3:
        print('yes')
        break
    print('循环数据', li)
else:
    print('没有循环数据')
print('完成循环')

# range()函数
for i in range(5):
    print(i)

for i in range(5, 9):
    print(i)

for i in range(0, 10, 3):
    print(i)

for i in range(-10, -100, -30):
    print(i)

a = [1, 2, 3, 4]
for i in range(len(a)):
    print(i, a[i])

print(list(range(5)))

# break和continue语句及循环中的else子句
for i in 'runppb':
    if i == 'p':  # 字母为p时，结束循环
        break
    print('当前字母为：', i)

for i in 'runppb':
    if i == 'p':  # 字母为p时，跳过输出，然后继续下一轮
        continue
    print('当前字母为', i)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=',  x, '*', n // x)
            # break
    else:
        print(n, '是质数')

print(2 % 2)

# pass语句，是空语句，为了保持程序结构的完整性，
# 不做任何实行，一般用做占位语句
for s in 'runoob':
    if s == 'o':
        pass
        print('执行pass块')
    print('当前字母：', s)
print('bye')

for char in 'PYTHON STRING':
    # if char == ' ':
    #     break
    # print(char, end='')
    if char == 'O':
        continue
    print(char, end='')

# for char in 'PYTHON STRING':
#     if char == ' ':
#         break
#     print(char, end='')
#     if char == 'O':
#         continue


