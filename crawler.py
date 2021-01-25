import requests
from bs4 import BeautifulSoup
# 生成一个response对象
# response = requests.get('https://www.zhihu.com')
# response.encoding = response.apparent_encoding  # 设置编码格式
# print('状态码：' + str(response.status_code))  # 打印状态码
# print(response.text)  # 取出爬取的信息

# response = requests.get('http://httpbin.org/get?name=hezhi&age=20')  # get方法
# response = requests.post("http://httpbin.org/post")  #post方法访问
# response = requests.put("http://httpbin.org/put")  # put方法访问
# print(response.status_code)
# print(response.text)

# response = requests.get("http://www.zhihu.com")  # 第一次访问知乎，不设置头部信息
# print("第一次,不设头部信息,状态码:" + str(response.status_code))  # 没写headers，不能正常爬取，状态码不是 200
# # 下面是可以正常爬取的区别，更改了User-Agent字段
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
# }  # 设置头部信息,伪装浏览器
# response = requests.get("http://www.zhihu.com", headers=headers)  # get方法访问,传入headers参数，
# print(response.status_code)  # 200！访问成功的状态码
# print(response.text)

# import cookielib3
# import urllib3
# url = 'http://www.baidu.com'
# response1 = urllib3.urlopen

if __name__ == '__main__':
    target = 'http://www.748219.com/meiwen/13625.html'
    req = requests.get(url=target)
    req.encoding = req.apparent_encoding
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_='article')  # 筛选出正文，class属性是article
    # texts = bf.find_all('div', 'box')
    print(texts[0].text)
    # texts = bf.find_all('a')
    # for t in texts:
    #     print(t)
    #     print(t.string)
    #     print(type(t.string))
    # print(html)
    # print('********************')
    # print(bf.head.contents)















