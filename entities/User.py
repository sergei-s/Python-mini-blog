from google.appengine.ext import db
from utils import pw

__author__ = 'ssav'

class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    email = db.StringProperty(required=False)

    @classmethod
    def get_by_name(cls, username):
        return User.gql('WHERE username = :username', username=username)

    @classmethod
    def get_by_email(cls, email):
        return User.gql('WHERE email = :email', email=email)

    @classmethod
    def register(cls, username, password, email = None):
        pw_hash = pw.make_pw_hash(username, password)
        user = User(username = username, password = pw_hash, email = email)
        user.put()