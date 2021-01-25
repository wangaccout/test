import sys

# while True:
#     try:
#         x = int(input('请输入一个数字：'))
#         break
#     except ValueError:
#         print('您输入的不是数字，请再次尝试输入')

# try:
#     f = open('test.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print('OS error:{0}'.format(err))
# except ValueError:
#     print('Could not convert data to an interger')
# except:
#     print('Unexpected error:', sys.exc_info()[0])
#     raise

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         print('haha')
#         f.close()

def this_fails():
    x = 1/5
#
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)

# list1 = [1, 2, 3]
# for i in list1:
#     try:
#         print(i)
#     except:
#         print('no')
#     else:
#         print('ok')


# try:
#     this_fails()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('test1.txt') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print('这句话，无论是否异常都执行')
#
# x = 11
# if x > 5:
#     raise Exception('x不能大于5.x的值为：{}'.format(x))

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)

