from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

html_content = urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html_content, "html.parser")
ul = soup.find("table", id = "tableContent")
# print(ul.prettify())

ul2 = ul.find_all("td", "b_r_c")

list_1 =[]
print(len(ul2))

# for i in ul2:
#     data = {}
#     data["content"] = ul2[i].string
#     number = i.string

#     print(number)

# for i in range(4)