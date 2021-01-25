import sys
# 迭代器 iter()  next()
# list = [1, 2, 3, 4]
# it = iter(list)
# print(next(it))
# print(next(it))
#
# li = iter(list)
# for x in li:
#     print(x, end=' ')
#
# list1 = [11, 12, 13, 14]
# for i in list1:
#     print(i, end=' ')

# lt = iter(list)
# while True:
#     try:
#         print(next(lt))
#     except StopIteration:
#         sys.exit()


class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration  # StopIteration 异常用于标识迭代的完成,防止出现无限循环

myclass = MyNumber()
myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
for x in myiter:
    print(x)

# 生成器 使用了yield的函数被称为生成器（generator）
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)  # 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        sys.exit()

