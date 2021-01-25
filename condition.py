# if语句
num1 = 1
if num1:
    print('表达式条件为true')
    print(num1)

num2 = 0
if num2:
    print('表达式条件为true')
    print(num1)
print('bye')

age = int(input('请输入年龄'))
if age <= 0:
    print('你在逗我吧')
elif age == 1:
    print('相当于人的14岁')
elif age > 2:
    human = 22 + (age - 2) * 5
    print('对应人类的年龄：', human)
input('点击 enter 退出')

# if嵌套
num = int(input('请输入一个数字： '))
if num % 2 == 0:
    if num % 3 == 0:
        print('可以整除2和3')
    else:
        print('不可以整除2和3')
else:
    if num % 3:
        print('可以整除3，不能整除2')
    else:
        print('不能整除2和3')