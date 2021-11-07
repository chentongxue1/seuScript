import urllib.request
import urllib.parse
import ssl
import http.cookiejar
import urllib
import pytesseract
from PIL import Image


ssl._create_default_https_context = ssl._create_unverified_context

url='http://ids1.seu.edu.cn/amserver/UI/Login'

userid = input("220205480")
password = input("cz238116154")

postdata1 = urllib.parse.urlencode({	
	'IDToken1':userid, 
 'IDToken2':password,
 'IDButton':'Submit',
 'goto':'http://yuyue.seu.edu.cn/eduplus/order/initOrderIndex.do?sclId=1',
 'gx_charset':'utf-8'
}).encode('utf-8')



req = urllib.request.Request(url,postdata1)
req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
data = opener.open(req).read()



urllib.request.urlretrieve('http://yuyue.seu.edu.cn:80/eduplus/control/validateimage', 'validateimage.jpg')  
img = Image.open('validateimage.jpg')
s = pytesseract.image_to_string(img)

reservetime = input("2021-11-17 :00-18:00)：")
item = input("7")  #（7代表乒乓球，10代表羽毛球）
inuserid = input("120542：")
phone = input("13337804870")

postdata2 = urllib.parse.urlencode({	
	'orderVO.useTime':reservetime, 
	'orderVO.itemId':item,
	'orderVO.useMode':'2',
	'useUserIds':inuserid,
	'orderVO.phone':phone,
	'validateCode':s,
}).encode('utf-8')

url2="http://yuyue.seu.edu.cn/eduplus/order/order/order/insertOredr.do?sclId=1"
req2 = urllib.request.Request(url2,postdata2)
req2.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")
data = opener.open(req2).read()

print(data)
