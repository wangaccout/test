from urllib import request

# 读和写文件
try:
    f = open('test.txt', 'r+')
    # f = open('test.txt', 'a')
    f.write('哈哈123伐柯伐柯反反复复减肥方法')
    f.seek(0)
    str1 = f.read()
    # f.seek(0)
    # str2 = f.readline(5)
    # f.seek(0)
    # str3 = f.readlines()
    # print(str1)
    # print(str2)
    # print(str3)
    # print(f.encoding)
finally:
    if f:
        f.close()

with open('test.txt', 'r+') as fil:
    print(fil.readlines())

# respone = request.urlopen("http://www.baidu.com/")  # 打开网站
# fi = open("project.txt", "w")  # open一个txt文件
# page = fi.write(str(respone.read()))  # 网站代码写入
# fi.close()

# input默认输入的为str格式，若用数学计算，需要转换格式
# a = input('请输入数字a：')
# print(a*2)
# b = int(input('请输入数字b：'))
# print(b*2)

# 以下是文件操作中常用的一些方法：

# print(f.readline())    # 打印一行
# print(f.readline(5))   # 打印前5个字符
# print(f.tell())        # 打印当前指针位置
# print(f.read())        # 读完文件后，指针在最尾处
# f.seek(0)              # 如要重头到尾再读，文件指针须先回到文件头(0-文件头,默认值; 1-当前位置; 2-文件尾)
# print(f.read())        # 重读文件
# print(f.encoding)      # 打印当前使用的字符编码
# print(f.name)          # 打印文件名
# print(f.flush())       # 刷新
# f.truncate()           # 清空文件
# f.truncate(12)         # 从头开始，第12个字符后截断并清除
# f.close()              # 关闭文件