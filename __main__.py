from auth import auth
from lxml import html
import urllib2

email = 'OLOLO' # почта от акка
password = 'OLOLO' #пароль от акка
vkID = '2951857'
scope = 'audio'

#tehToken = 'a85ad24df9e5dc9aa92044ed47a95252748a97fa97f58cdf9e66a1a1e68cd1e8f4e2473'
tehToken, userID = auth(email, password, vkID, scope)
print(tehToken)
tehURL = "https://api.vkontakte.ru/method/audio.get.xml?uid=" + userID + "&access_token=" + tehToken
page = urllib2.urlopen(tehURL)
rawHTML = page.read()
try:
    doc  = html.document_fromstring(rawHTML)
except html.etree.ParserError:
    print('Parser error.')

#doc  = html.document_fromstring(tehURL)

artistMas = []
number = 0

print(doc.cssselect('artist').__len__())
for artist in doc.cssselect('artist'):
    artistMas.append(artist.text)
    number += 1
try:
    print(artistMas[0], artistMas[1])
except:
    print('Fail.')