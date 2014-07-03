from google.appengine.ext import db

class Station(db.Model):
    callsign = db.StringProperty(required=True)
    frequency = db.StringProperty(required=True)
    city = db.StringProperty(required=True)

class Radiorequest(db.Model):
    #PKID = db.StringProperty(default="")
    #specimens = db.ListProperty(db.Key)
    #species = db.ReferenceProperty(Species)
    request = db.StringProperty(required=True,multiline=True)
    time = db.DateTimeProperty(auto_now_add=True)
    station = db.ReferenceProperty(Station, collection_name='requests')
