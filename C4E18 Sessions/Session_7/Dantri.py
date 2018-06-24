# # 1. Download webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

# # 1.1. Create a connection
url = "http://dantri.com.vn"

# connection = urlopen(url) .read().decode('utf-8')
# connection = urlopen(url) 

# print(html)

# 1.2. Read
# data = connection.read()
# print(data)

# 1.3. decode
# html_content = data.decode("utf-8")


# @ ban viet tat ngan gon @
html_content = urlopen(url).read().decode("utf-8")
# print(html_content)

# @Save html content to file
# @da luu file roi
# f = open("./dantri.html", "wb")
# f.write(html_content)
# f.close()

# 2. Extract ROI (region of interest)
# chuyen dinhdang vesoup
# beautiful soup co the phan tich nhieu dinh dang: html, xhtml, xml
soup = BeautifulSoup(html_content,"html.parser")
# lam dep html
# print(soup.prettify())

# ul: bat soup
ul = soup.find("ul","ul1 ulnew")
# Ten the - dac diem (class)
# ko viet dinh danh dac diem >>> mac dinh la class =
# li la thia soup
li_list = ul.find_all("li")
# print(ul.prettify())


dictionary = []

for li in li_list:
    item = {}
#     print(li.prettify())
#     print("*" *20)
#     h4 = li.find("h4")
#     a = h4.find("a")
    h4 =li.h4
    a = h4.a 
    # Viet gon lai nua
    # a = li.h4.a
    title = a.string
    link = url + a["href"]
    # print(a.string)
    # print(url +a["href"])
    item['value'] = link
    item["link"] = title
    dictionary.append(item)

    # print(dictionary)
    # print(type(dictionary))
   


pyexcel.save_as(records= dictionary, dest_file_name="link.xlsx")

    




# 3. Extract info
