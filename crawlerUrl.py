import requests
from bs4 import BeautifulSoup



if __name__ == '__main__':
    server = 'http://www.748219.com/meiwen/'
    target = 'http://www.748219.com/meiwen/13625.html'
    req = requests.get(url=target)
    req.encoding = req.apparent_encoding
    html = req.text
    bf = BeautifulSoup(html)
    # print(bf)
    # texts = bf.find_all('div', class_='article')  # 筛选出正文，class属性是article
    texts = bf.find_all('div', class_='box')
    a_bf = BeautifulSoup(str(texts))
    li = a_bf.find_all('li')
    lli = BeautifulSoup(str(li))
    a = lli.find_all('a')
    # print(a)
    # print(texts)
    # texts = bf.find_all('span', class_='next')
    # print(texts)
    # a_df = BeautifulSoup(str(texts[0]))
    # print(a_df)
    # a = bf.find_all('a')
    for each in a:
        # print(each)
        print(each.string, each.get('href'))


















