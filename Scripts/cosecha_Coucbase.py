from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator

import json
import random

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


###Credenciales de la cuenta de Twitter########################
ckey = "KwQZ0i9qHMhX5A7fc2SQn6nXI"
csecret = "fGUubxQDxiMJBMldIZ9BwJKI4fkg6ak5YrCx6rjZh8G7EGBl1Y"
atoken = "1223459511312228354-tq7bIl3MS88RynWBGzZa7xSGhA24rB"
asecret = "qEdRrMoJhYjAJ0UEYwzB82QiAONEP5C56HUqWSzUP4mu7"
#####################################

cluster = Cluster('couchbase://localhost')
authenticator = PasswordAuthenticator('andres', 'andres')
cluster.authenticate(authenticator)
cb = cluster.open_bucket('eventos')

class listener(StreamListener):

    def on_data(self, data):
        dictTweet = json.loads(data)

        idc = "id_"
        nums = random.randrange(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
        num = nums

        num = num + 1
        val = idc + "_" + str(num)

        try:

            dictTweet["_id"] = str(dictTweet['id'])
            #Antes de guardar el documento puedes realizar parseo, limpieza y cierto analisis o filtrado de datos previo
            #a guardar en documento en la base de datos
            #doc = db.save(dictTweet) #Aqui se guarda el tweet en la base de couchDB
            doc = cb.insert(val ,dictTweet)

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


#Aqui se define el bounding box con los limites geograficos donde recolectar los tweets
twitterStream.filter(track=["evento","noticia","mundial"])
#twitterStream.filter(track=["Barcelona","Champions"],locations=[-81.66,-4.83,-75.42,1.54])
#twitterStream.filter(locations=[-81.66,-4.83,-75.42,1.54])


