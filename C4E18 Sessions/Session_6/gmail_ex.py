# >>> gmail = GMail('A.User <user@gmail.com>','password')
# >>> msg = Message('Test Message',to='xyz <xyz@xyz.com>',text='Hello')
# >>> gmail.send(msg)

from gmail import GMail
from gmail import Message
from random import choice

# gmail = GMail("printwork93@gmail.com","printpurpose")
# msg = Message("Test message 1", to = "20130075@student.hust.edu.vn", text = "Hello")
# gmail.send(msg)

html_content = """
 <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Cộng h&ograve;a X&atilde; hội Chủ nghĩa Việt Nam</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Độc lập - Tự do - Hạnh ph&uacute;c</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>&nbsp; &nbsp; &nbsp;ĐƠN XIN NGHỈ HỌC</strong></p>
<p>Hi Tuấn Anh,</p>
<p>H&ocirc;m nay anh {{sickness}} n&ecirc;n nghỉ buổi học tối nay nh&eacute;.</p>
<p>Thank you.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
"""

# placeholder: thay noi dung trong content
list_nghi = ["di choi voi gai", "chan hoc", "me a di khoa cua nen a bi nhot trong nha"]
reason = choice(list_nghi)
new_content = html_content.replace("{{sickness}}",reason)

gmail = GMail("printwork93@gmail.com","printpurpose")
msg = Message("Test message 1",
    to = "20130075@student.hust.edu.vn",
    html = new_content)

# s ="hom nay a bi {{sickness}}"
# new_str = s.replace("{{sickness}}","gay chan")


gmail.send(msg)