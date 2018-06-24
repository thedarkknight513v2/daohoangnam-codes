from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL


# Create a connection, read & decode
url ="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

html_content = urlopen(url).read().decode("utf-8")
# f = open("./cafef.html", "wb")
# f.write(html_content)
# f.close()

# Extract ROI
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())

ul0 = soup.find("div", style = "overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
# print(ul)
ul1 = ul0.find("table", id ="tableContent")
# print(ul1.prettify())
ul2 = ul1.find_all("tr", "r_item ")

for i in ul2:
    ul3 = i.find("td", style = "width:32%;color:#014377;font-weight:bold;")
    print(ul3)
    # print(ul3)

    # fsli_name_1 = ul3.string
    # print(fsli_name_1)

# for i in ul1:
#     ul2 = ul1.find_all("tr", "r_item ")
# # print(ul2)

# # for i in ul2:
#     dictionary = {}
#     td = ul2.find("td", "b_r_c")
#     # fsli_1 = td.string
#     print(td)


# for li in li_list3:
#     dictionary = {}
#     h3 = li.find("h3")
#     song_name = h3.string
#     # print(song_name)
#     h4 = li.find("h4")
#     artist_name = h4.string
#     # print(artist_name)
#     combined_search_item = "{0} {1}".format(song_name,artist_name)
#     download_list.append(combined_search_item)
    
#     dictionary["artist"] = artist_name
#     dictionary["song name"] = song_name
#     top_chart_list.append(dictionary)

# pyexcel.save_as(records =top_chart_list, dest_file_name = "top chart.xlsx")

# for i in download_list:
#     options = {
#             "default_search": "ytsearch",
#             "max_downloads": 1
#         }
#     dl = YoutubeDL(options)
#     dl.download([i])





