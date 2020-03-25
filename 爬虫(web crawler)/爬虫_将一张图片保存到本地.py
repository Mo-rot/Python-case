import requests

# 模拟浏览器，避开反爬
headers = {'user-agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
           ' (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

# 请求单独一张图片的url
r = requests.get("https://photo.tuchong.com/1438212/f/47402388.jpg", headers=headers)

# 将图片保存到C盘根目录
with open(r"C:\1.jpg", 'wb') as f:
    f.write(r.content)
