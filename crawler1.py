# -*- coding:UTF-8 -*-
import requests
import sys
from bs4 import BeautifulSoup

if __name__ == '__main__':

    head_url = 'https://www.biqukan.com'
    url = 'https://www.biqukan.com/1_1094/'
    res = requests.get(url=url)
    res.encoding = 'gbk'
    bf = BeautifulSoup(res.text, features="html.parser")
    div = bf.find_all('div', class_='listmain')
    bf_a = BeautifulSoup(str(div[0]))
    a = bf_a.find_all('a')
    i = 0
    si = len(a[13:23])
    print("开始下载：")
    for each in a[13:23]:
        target = head_url + each.get('href')
        respons = requests.get(url=target)
        respons.encoding = 'gbk'
        bfs = BeautifulSoup(respons.text, features="html.parser")
        texts = bfs.find_all('div', class_='showtxt')
        with open("一念永恒3.txt", mode='a', encoding='utf-8') as f:
            f.write('\n\n' + each.string + '\n')
            f.write(texts[0].text.replace('\xa0' * 8, '\n'))
            f.close()
        with open("mulu.txt", mode='a', encoding='utf-8') as ff:
            ff.write(each.string + '\n')
            ff.close()
        sys.stdout.write(" \r  已下载:%.3f%%" % float(i / si) + '\r')
        sys.stdout.flush()
        i = i + 1
        if i == si:
            break
    print("下载完成")