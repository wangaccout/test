from datetime import datetime as dt
import sys
import time

while True:
    a = dt.now()
    sys.stdout.write("\r{0}".format(a))
    sys.stdout.flush()
    time.sleep(1)
#
# i = 0
# for i in range(20):
#     time.sleep(1)
#     sys.stdout.write("\r# Process: %0.1f %%" % (float(i + 1) / float(20) * 100))
#     sys.stdout.flush()
# a, b = 0, 1
# while b < 10:
#     print(b, end=',')
#     a, b = b, a + b
#
# sys.stdout.write('hfhghgh')

# for i in range(100):
#     percent = i / 100
#     sys.stdout.write("\r{0}{1}".format("|" * i, '%.2f%%' % (percent * 100)))
#     sys.stdout.flush()
#     time.sleep(1)