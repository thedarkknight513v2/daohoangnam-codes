# # 1. Download webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup
# import pyexcel

# # 1.1. Create a connection
url = "http://dantri.com.vn"

# connection = urlopen(url) .read().decode('utf-8')
# connection = urlopen(url) 



# # 1.2. Read
# data = connection.read()
# print(data)

# 1.3. decode 
# html_content = data.decode("utf-8")
# print(html_content)

html_content = urlopen(url).read()
print(html_content)

# Save file
f = open("./dantri.html", "wb")
f.write(html_content)
f.close()
