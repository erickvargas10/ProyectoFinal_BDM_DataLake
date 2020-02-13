import couchdb  #Libreria de CouchDB (requiere ser instalada primero)
import json  #Libreria para manejar archivos JSON

import requests # pip install requests


ACCESS_TOKEN = 'EAAGyudrPioYBAH0APAJ3gCSmZCnt2NGaMei4dOZCCLxfgsNnsrmyesv4ZBv9la8hUhIRZAET3b2LYgKdBggZAHyZB5Xrw3ei0' \
               'ZAEmSe4LkwgNWYtoNV1ZAU612kdilOGXG8WY5Tf4ZCrxX7R3BPPZAgaaVLBle4X5LIUUoW28orOsCIXKU5Bfy4xxZBAF7bMdt2tL' \
               'neWXJLWiYHjG62wsnZAMHxTyVGWcnd1ZAlUqQSw1eQzJvgZDZD'

base_url = 'https://graph.facebook.com/2735041006564405/'
fields = 'description%2Cis_expired%2Ctype%2Ccreated_time'
#fields = 'category'


#description%2Cis_expired%2Ctype%2Ccreated_time


url = '%sposts?fields=%s&access_token=%s&limit=25&__paging_' \
      'token=enc_AdBZB9aJQyR3veIwgDBTachBFZAnC1cSW41Qp0jqIlSHaJ7RtlKy0CIp6Lecbbg872iK0D27lLC5SBZAiyUnyIpK4ZBGUrm0ZBzjMFD4G7tYyNRq3LQZDZD&until=1419309164' % \
(base_url, fields, ACCESS_TOKEN,)

server = couchdb.Server('http://localhost:5984/')
try:
    #Si no existe la Base de datos la crea
    db = server.create('temapropio')
except:
    #Caso contrario solo conectarse a la base existente
    db = server['temapropio']

content = requests.get(url).json()

db.save(content)












