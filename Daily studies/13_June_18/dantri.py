VI. Extract website data
1. Download webpage

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

1.1. Create a connection
url = "http://dantri.com.vn"
connection = urlopen(url) 

1.2. Read
data = connection.read()
print(data)

1.3. decode 
html_content = data.decode("utf-8")

(ban viet tat ngan gon (from 1.1 to 1.3): 
html_content = urlopen(url).read().decode("utf-8") )

1.4. Save html content to file (google cụm từ input - output)
f = open("./dantri.html", "wb")
f.write(html_content)
f.close()

2. Extract ROI (region of interest)
2.1. Chuyển định dạng về soup. BeautifulSoup có thể phân tích nhiều định dạng (html, xhtml, xml)
soup = BeautifulSoup(html_content,"html.parser")

2.2. làm đẹp html (tab lại cho đẹp)
print(soup.prettify())

2.3. Tìm bát súp (trong trường hợp này là thẻ ul)
(tìm thẻ ul, class = "ul1 ulnew")
sử dụng: find/find_all: Ten the - dac diem (class)
Nếu không viết định danh attribute thì mặc định là class (xem trong documentation ở crummy.com)
ul = soup.find("ul",class = "ul1 ulnew")

2.4. Tìm tiếp ROI
li_list = ul.find_all("li")

list_1 = []

for li in li_list:
    item = {}

Có 3 cách tìm:
C1:
    h4 = li.find("h4")
    a = h4.find("a")
C2:
    h4 =li.h4
    a = h4.a 
C3:
    a = li.h4.a

    title = a.string
    link = url + a["href"]
    # print(a.string)
    # print(url +a["href"])
    item['value'] = link
    item["link"] = title
    lsit_1.append(item)
   
3. Extract info
pyexcel.save_as(records= dictionary, dest_file_name="link.xlsx")

    




