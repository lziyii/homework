#以人人网为例
import requests

session = requests.session()
url = "http://www.renren.com/PLogin.do"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36"}
date = {
    "email": "15869117206",
    "password": "a588181"
}
session.post(url, headers=headers, data=date)
url1 = "http://www.renren.com/966470757/profile"
session.get(url1)