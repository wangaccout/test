# Python中只有模块（module），类（class），函数（def，lambda）才会引入新的作用域
# 其他代码块（如 if/elif/else、try/except、for/while等）不会引入新的作用域，浙西的语句内定义 的变量，外部也可以访问

def test():
    msg_inner = 'I am tom'
    print(msg_inner)
test()
# print(msg_inner)  # 报错，局部变量只能在函数中用

# if True:
#     msg = 'hello'
# print(msg)

total = 0  # 这是一个全局变量
def sum(arg1, arg2):
    total = arg1 + arg2  # 局部变量
    print('函数内部是局部变量：', total)
    return total
sum(10, 20)
print('函数外是全局变量：', total)

# 当内部作用域想修改外部作用域的变量时，用global和nonlocal关键字
num = 1
def fun1():
    global num  #使用global关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)

# 修改嵌套作用域（enclosing作用域，外层非全局作用域）中的变量，需要nonlocal关键字
def outer():
    num = 10
    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()

a = 10
def test():
    # global a
    a = a + 1
    print(a)
test()  # 报错





