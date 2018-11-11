import requests
import os
import re

print("百度图片爬取器")
print("author:Shi Yu,2018.5.9\nVer.1.1 203专用版")
print("使用说明：输入要搜索的物体之后，将自动在当前目录下创建一个文件夹，然后把图片自动保存下来）")
search_content = input("请输入要找的人的姓名（你百度搜什么这里就输入什么）：")

root = os.getcwd() +"/" + search_content +'/'
if not (os.path.exists(root)):
        os.mkdir(search_content)
#root = "/home/shiyu/requests/" + search_content +'/'
pages = eval(input("请输入爬取的页数,每页20张："))
#url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=detail&fr=&hs=0&xthttps=111111&sf=1&fmq=1524232126024_R&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word="

headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
#url = url + search_content
#search_content
#hd = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
#path = root + url.split('/')[-1]
for k in range(0, pages):
	url = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=" + search_content + "&pn=" + str(int(20*k)) + "&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0"
	print(url)
	r = requests.get(url, headers, timeout = 10)
	r.encoding = r.apparent_encoding

	if(r.status_code == 200):
		response = r.text  
		#"http://shiyu.com.jpegsdsdsdsdshjbxcvmncbvzytyusfhttp://shiyu.cn.jpg"
		#f.write(r.text)
		#f.close()
		#try:
		urls = re.findall(r"(http://.*?\.(jpg|jpeg))", response)
		for i in range(0, len(urls)):
			print(urls[i][0])
			try:
				m = requests.get(urls[i][0], headers, timeout = 10)
			except:
				print("timeout!!!")
				continue
			path = root + urls[i][0].split('/')[-1]
			print(path)
			if not (m.status_code == 200):
				print(m.status_code,"error")
				continue
			with open(path, 'wb') as f:
				f.write(m.content)
				f.close()
				print("saved successfully")
		#except:
		#	print("fail!!!")
	else:
		print(r.status_code,"error")


