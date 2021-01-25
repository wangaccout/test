class MyClass:
    """一个简单的类实例"""
    i = 123
    def f(self):
        return 'hello world'

x = MyClass()  # 实例化类
# 访问类的属性和方法
print('MyClass类的属性i为：', x.i)
print('MyClass类的方法f输出为：', x.f())


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)

# self代表类的实例
class Test:
    def prt(self):
        print(self)  # self代表的是类的实例，代表当前对象的地址
        print(self.__class__)  # self.class指向类
t = Test()
t.prt()
# self 不是Python关键字，换成run也可以正常执行
class Test1:
    def prt(run):
        print(run)
        print(run.__class__)
t = Test1()
t.prt()

# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('%s说：我%d岁,体重%d斤' % (self.name, self.age, self.__weight))

# 实例化类
# p = people('tom',10,30)
# p.speak()

class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g
    # 覆写父类的方法
    def speak(self):
        print('%s说：我%d岁了，我在读%d年级' % (self.name, self.age, self.grade))
# s = student('ken', 10, 60, 3)
# s.speak()

class speaker():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print('我叫%s,我是一个演说家，我演讲的主题是%s' % (self.name, self.topic))

# 多重继承
class sample(speaker, student):
    # a = ''
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)
test = sample('Tim', 20, 90, 3, 'python')
test.speak()  # 方法同名，默认调用的是在括号中排前的父类方法

# 方法重写
class parent:
    def myMethod(self):
        print('调用父类方法')

class child(parent):
    def myMethod(self):
        print('调用子类方法')
c = child()
c.myMethod()  # 子类调用重写方法
super(child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法

class justCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = justCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量

class site:
    def __init__(self, name, url):
        self.name = name
        self.__url = url
    def who(self):
        print('name:', self.name)
        print('url:', self.__url)
    def __foo(self):
        print('这个是私有方法')
    def foo(self):
        print('这是公共方法')
        # self.__foo()

x = site('百度', 'baidu.com')
x.who()
x.foo()
# x.__foo()  # 报错

class vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'vector(%d, %d)' % (self.a, self.b)
    def __add__(self, other):
        return vector(self.a + other.b, self.b + other.a)

v1 = vector(2, 10)
v2 = vector(5, -2)
print(v1 + v2)




