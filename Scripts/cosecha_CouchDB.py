import couchdb  #Libreria de CouchDB (requiere ser instalada primero)
from tweepy import Stream  #tweepy es la libreria que trae tweets desde la API de Twitter (requiere ser instalada primero)
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json  #Libreria para manejar archivos JSON

###Credenciales de la cuenta de Twitter########################
#Poner aqui las credenciales de su cuenta privada, caso contrario la API bloqueara esta cuenta de ejemplo
ckey = "KwQZ0i9qHMhX5A7fc2SQn6nXI"
csecret = "fGUubxQDxiMJBMldIZ9BwJKI4fkg6ak5YrCx6rjZh8G7EGBl1Y"
atoken = "1223459511312228354-tq7bIl3MS88RynWBGzZa7xSGhA24rB"
asecret = "qEdRrMoJhYjAJ0UEYwzB82QiAONEP5C56HUqWSzUP4mu7"
#####################################

class listener(StreamListener):

    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet) #Aqui se guarda el tweet en la base de couchDB
            print ("Guardado " + "=> " + dictTweet["_id"])
        except:
            print ("Documento ya existe")
            pass
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

server = couchdb.Server('http://localhost:5984/')
try:
    #Si no existe la Base de datos la crea
    db = server.create('toptwitteros4')
except:
    #Caso contrario solo conectarse a la base existente
    db = server['toptwitteros4']

#Aqui se define el bounding box con los limites geograficos donde recolectar los tweets
#twitterStream.filter(track=["Barcelona","Champions"],locations=[-78.586922,-0.395161,-78.274155,0.021973])
twitterStream.filter(locations= [-79.220346,-0.289352,-79.112542,-0.230473])

####################################

#Ambato = [-78.66919,-1.31054,-78.560014,-1.200016]

#Cuenca = [-79.069505,-2.946317,-78.932176,-2.853739]

#StoDomingo = [-79.220346,-0.289352,-79.112542,-0.230473]





