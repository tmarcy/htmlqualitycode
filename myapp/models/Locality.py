from google.appengine.ext import ndb


class Locality(ndb.Model):
    name = ndb.StringProperty()
    counter = ndb.IntegerProperty(default=0)
