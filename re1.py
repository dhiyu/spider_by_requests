import re

url = "http://shiyu.com.jpegsdsdsdsdshjbxcvmncbvzytyusfhttp://shiyu.cn.jpg"
try:
	urls = re.findall(r"(http://.*?\.(jpg|jpeg))", url)
	for i in range(0, len(urls)):
		print(urls[i][0])
except:
	print("fail!!!")
