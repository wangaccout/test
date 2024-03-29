import time
import calendar
ticks = time.time()  # 用于获取时间戳，输出为浮点数
print('当前时间戳为：', ticks)

# 将浮点数的时间戳转换为时间元组
localtime = time.localtime(time.time())
print('本地时间为：', localtime)

# 获取格式化时间
localtime = time.asctime(time.localtime(time.time()))
# localtime = time.asctime(ti)
print('本地时间为：', localtime)

# 格式化日期
# 格式化成2020-10-28 11:11:11形式
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# 格式化成Sat Mar 28 11:11:11 2020形式
print(time.strftime('%a %b %d %H:%M:%S %Y', time.localtime()))
# 将格式字符串转换为时间戳
a = 'Wed Oct 28 11:20:20 2020'
print(time.mktime(time.strptime(a, '%a %b %d %H:%M:%S %Y')))

# 获取某月日历
cal = calendar.month(2020, 10)
print('以下输出2020年10月的日历')
print(cal)

print(time.perf_counter())  # 返回系统运行时间
print(time.process_time())  # 返回进程运行时间

# 进度条
scale = 50
print('执行开始'.center(scale//2, '-'))  # .center()控制输入的样式，宽度为50//2，汉子居中，两侧填充 -
start = time.perf_counter()
# 调用一次perf_counter()，从计算机系统里随机选一个时间点A，计算其距离当前时间点B1有多少秒。
# 当第二次调用该函数时，默认从第一次调用的时间点A算起，距离当前时间点B2有多少秒。
# 两个函数取差，即实现从时间B1到B2的计时功能
for i in range(scale+1):
    a = '*' * i  # i个长度的 * 符号
    b = '.' * (scale-i)  # scale-i 个长度的 . 符号。 符号 * 和. 总长度为50
    c = (i/scale)*100  # 显示当前进度，百分之多少
    dur = time.perf_counter() - start  # 计时，计算进度条走到某一百分比的用时
    print('\r{:^3.0f}%[{}->{}]{:.2F}s'.format(c, a, b, dur), end='')
    # \r用来在每次输出完成后，将光标移至行首，保证进度条始终在同一行输出，即在一行不断刷新的效果；
    # {:^3.0f} 输出格式为居中，占3位，小数点后0位，浮点型数，对应输出的数为c;
    # {}对应输出的数为a; {}对应输出的数为b;
    # {:.2f} 输出有两位小数的浮点数，对应dur; end=''用来保证不换行，不加这句默认换行
    time.sleep(0.1)  # 在输出下一个百分之几的进度前，停止0.1秒
print('\n'+'执行结果'.center(scale//2, '-'))














