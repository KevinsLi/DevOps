import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')


CSRF_ENABLED = True
SECRET_KEY = 'lyao36843'

OPENID_PROVIDERS = [
    {'name':'google','url':'https://www.google.com/accounts/o8/id'},
    {'name':'yahoo','url':'https://me.yahoo.com'},
    {'name':'aol','url':'http://openid.aol.com/<username>'},
    {'name':'flickr','url':'http://www.flickr.com/<username>'},
    {'name':'myopenid','url':'https://www.myopenid.com'}]
