from google.appengine.ext import ndb


class Employees(ndb.Model):
    name = ndb.StringProperty()
    tps_reports = ndb.IntegerProperty()
