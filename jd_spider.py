import requests
url = "https://search.jd.com/Search?keyword=%E5%85%85%E6%B0%94%E5%A8%83%E5%A8%83&enc=utf-8&suggest=1.def.0.V10&wq=chongqiwa&pvid=c89999b1341a47d7b93d69f8fa0ee650" #"https://item.jd.com/1263013576.html"
try:
	r = requests.get(url)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text)
except:
	print("爬取失败！！！")
