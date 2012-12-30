from google.appengine.ext import db

__author__ = 'ssav'

class Post(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_all_order_by_date(cls):
        return Post.gql('ORDER BY created DESC')

    def as_dict(self):
        time_fmt = '%c'
        d = {'title': self.title,
             'content': self.content,
             'created': self.created.strftime(time_fmt)}
        return d