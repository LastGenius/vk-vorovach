from auth import auth
from lxml import html
import urllib2
import vkontakte

email = '123' # 
password = '123' #
vkID = '2951857'
scope = 'audio'

#tehToken = 'e103d0a5b0bcca78e09654dbd5e00b509cce026e0265a25b0bf64f889a2f6da22b9f40a'
#userID = 19237512
tehToken, userID = auth(email, password, vkID, scope)
print(tehToken, userID)
vk = vkontakte.API(token=tehToken)
sresult = vk.audio.search(q='Mozart', count=5)
tehURL = "https://api.vkontakte.ru/method/audio.get.xml?uid=" + userID + "&access_token=" + tehToken
page = urllib2.urlopen(tehURL)
rawHTML = page.read()
try:
    doc  = html.document_fromstring(rawHTML)
except html.etree.ParserError:
    print('Parser error.')

artistMas = []
number = 0

for artist in doc.cssselect('artist'):
    artistMas.append(artist.text)
    number += 1
try:
    print(artistMas[0], artistMas[1])
except:
    print('Fail.')