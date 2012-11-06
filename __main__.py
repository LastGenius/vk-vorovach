from auth import auth
from lxml import html

email = 'OLOLO'
password = 'OLOLO'
vkID = '123123123'
scope = 'photos'

tehToken = auth(email, password, vkID, scope)
tehURL = "https://api.vkontakte.ru/method/audio.get.xml?uid=" + vkID + "&access_token=" + tehToken
doc  = html.document_fromstring(tehURL)

artistMas = []
number = 0

for artist in doc.cssselect('artist'):
    artistMas.append(artist.text)
    number += 1
try:
    print(artistMas[0], artistMas[1], artistMas[2])
except:
    'Что-то пошло не так.'