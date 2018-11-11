#Python爬虫1.0:网页爬取时间测试-v1.0.py
import time
import requests
     
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return '成功'
    except:
        return '失败'
     
def main():
    print('请输入网址')
    url = input()
    print('请输入爬取次数')
    n = int(input())
    start = time.perf_counter()
    for i in range(n):
        getHTMLText(url)
        a = '*' * i
        b = '.' * (n-1 - i)
        c = (i / (n-1)) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
    print("\n爬取{}网站{}次,用时{:.2f}s".format(url,n,dur))
     
if __name__ == '__main__':
    main()
