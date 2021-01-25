import sys
import re
# str()：函数返回一个用户易读的表达形式
# repr():产生一个解释器易读的表达形式

s = 'Hello, Runoob'
print(str(s))
print(repr(s))

print(str(1/7))
print(repr(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
z = 'x 的值为： ' + str(x) + ',  y 的值为：' + str(y) + '...'
print(s)
print(z)

# repr()函数可以转移字符串中的特殊字符
hello = 'Hello, Runoo\nb'
print(str(hello))
print(repr(hello))
# repr()的参数可以是Python中的任何对象
print(repr((x, y, ('good', 'word'))))
w = repr((x, y, ('Google', 'Runoob')))
print(w)
# rjust()方法 将字符串靠右，并在左边填充空格;类似方法有ljust()和center()，zfill()在数字的左边填充0
for x in range(1, 5):
    print(repr(x).rjust(1), repr(x*x).rjust(2), end=' ')
    print(repr(x*x*x).rjust(3))

for x in range(2, 5):
    print('{0:1d}{1:3d}{2:4d}'.format(x, x*x, x*x*x))

# str.format()的基本使用
print('{}你好，“{}！”'.format('北京', '哈哈'))
print('{1} and {0}'.format(0, 1))
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))

# 读取键盘输入
str = input("请输入：")
if not re.match('^[a-z]*$', str):
    print('只能输入a-z')
    sys.exit(0)
elif len(str) > 5:
    print("最多5个字")
    sys.exit(1)
print('你输入的内容是：' + str)





