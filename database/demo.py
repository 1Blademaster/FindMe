
import firebase_admin
from firebase_admin import credentials, firestore
from datafile import data

cred = credentials.Certificate("firebase_creds.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

ref = db.collection('lobbies')

# hostID = 123
# numberofPlayers = 10
lobby = db.collection(u'lobbies').document(u'y6yXGwUSl0G4TiCOWBJZ')

# lobby.set({
#     u'hostID' : hostID,
#     u'NoOfPlayers': numberofPlayers,
# }, merge = True) 

# for r in ref.stream():
#     print(r.to_dict())

# lobby.update({
#     u'NoOfPlayers' : 5
# })

# for r in ref.stream():
#     print(r.to_dict())

# lobby.update({
#     u'NoOfPlayers' : firestore.DELETE_FIELD
# })

# for r in ref.stream():
#     print(r.to_dict())
