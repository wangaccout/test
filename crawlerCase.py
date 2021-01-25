import requests
import sys
from bs4 import BeautifulSoup

class downloader(object):
    def __init__(self):
        self.target = 'http://www.748219.com/meiwen/13625.html'
        self.names = []  # 存放章节名
        self.urls = []   # 存放章节链接
        self.nums = 0    # 章节数

    # 获取下载链接
    def get_download_url(self):
        req = requests.get(url=self.target)
        req.encoding = req.apparent_encoding
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_='box')
        a_bf = BeautifulSoup(str(texts))
        li = a_bf.find_all('li')
        lli = BeautifulSoup(str(li))
        a = lli.find_all('a')
        # a = bf.find_all('a')
        self.nums = len(a[4:10])
        for each in a[4:10]:
            self.names.append(each.string)
            self.urls.append(each.get('href'))
            # print(each.string, each.get('href'))
            # texts = each.find_all('div', class_='article')
            # print(texts[0].text)

    # 获取章节内容
    def get_contents(self, target):
        req = requests.get(url=target)
        req.encoding = req.apparent_encoding
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_='article')
        texts = texts[0].text
        return texts
        # print(texts)

    # 将爬取的文章内容写入文件
    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')
#
if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    # dl.get_contents()
    print('开始下载')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '一念.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write(' \r# 已下载：%.3f%%' % float(i/dl.nums) + '\r')
        sys.stdout.flush()
        # print('已下载：%.3f%%' % float(i / dl.nums))

    print('下载完成')
    # sys.stdout.write('已下载' )














