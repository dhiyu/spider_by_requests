import requests
import os
url = "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=544295208,706802747&fm=200&gp=0.jpg"
root = "/home/shiyu/requests/"
path = root + url.split('/')[-1]
print(path)
try:
	#if not os.path.exists(root):
	#	os.madir(root)
	#if not os.path.wxists(path):
	r = requests.get(url)
	print(r.status_code)
	with open(path, 'wb') as f:
		f.write(r.content)
		f.close()
		print("saved successfully")
	#else:
	#	print("document have existed")
except:
	print("fail!!!")
