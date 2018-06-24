# Basic usage:

# >>> gmail = GMail('A.User <user@gmail.com>','password')
# >>> msg = Message('Test Message',to='xyz <xyz@xyz.com>',text='Hello')
# >>> gmail.send(msg)

from gmail import GMail
from gmail import Message
from random import choice

# gmail = GMail("printwork93@gmail.com","printpurpose")
# msg = Message("Test message 1", to = "allmaterials513@gmail.com", text = "Hello")
# gmail.send(msg)

html = """
<p><strong>I already bought {{Games}}</strong></p>
"""

games = ["Diablo 3", "Uncharted 4", "Fifa 17", "Pes 17", "Horizon zero dawn", "Dragon Age inquisition GOTY", "The witcher 3", "Tekken 7", "GTA V"]
games_chosen = choice(games)
new_html = html.replace("{{Games}}", games_chosen)

gmail = GMail("printwork93@gmail.com","printpurpose")
msg = Message("Test message 1", to = "allmaterials513@gmail.com", html = new_html)
gmail.send(msg)


