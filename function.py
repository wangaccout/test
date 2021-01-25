# 函数
def func():
    print('ok')

func()

def Foo(x):
    if (x==1):
        return 1
    else:
        return x+Foo(x-1)

print(Foo(4))

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一个模块')

result = lambda x: x * x
print(result(5))

# 内置函数
print('{} {}'.format('hello', 'world'))  # 不设置指定位置，按默认顺序
print('{1} {0}'.format('hello', 'world'))  # 设置指定位置
print('姓名：{name}, 年龄{age}'.format(name='tom', age=12))
# 通过字典设置参数
site = {'name': 'tim', 'age': 18}
print('姓名：{name}，年龄：{age}'.format(**site))
# 通过列表索引设置参数
list = ['张三', 20]
print('姓名:{0[0]}, 年龄:{0[1]}'.format(list))  # 0是必须的
# 也可以向str.format()传入对象
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value为：{0.value}'.format(my_value))  # 0是可选的
# 数字格式化
print('{:.2f}'.format(3.1415926))