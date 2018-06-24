Example 7. Basic sending email using (pip install gmail)

from gmail import GMail
from gmail import Message
from random import choice

html_content = """
 abcxyz
"""

placeholder: thay noi dung trong content

list_nghi = ["dau bung", "dau dau", "cam cum"]
reason = choice(list_nghi)
new_content = html_content.replace("{{sickness}}",reason)

gmail = GMail("daohoangnam@gmail.com","thisnoexist")
msg = Message("Test message 1",
    to = "emailtosend@gmail.com",
    html = new_content)

gmail.send(msg)