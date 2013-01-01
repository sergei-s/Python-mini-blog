from google.appengine.ext import db
from google.appengine.api import memcache
import time

__author__ = 'ssav'



class Post(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    ALL_POSTS = 'all_posts'
    LAST_TIME_QUERIED = 'last_time'

    @classmethod
    def get_all_order_by_date(cls, update_cache = False):
        all_posts = memcache.get(cls.ALL_POSTS)
        if update_cache or all_posts is None:
            all_posts = Post.gql('ORDER BY created DESC')
            memcache.set(cls.ALL_POSTS, all_posts)
            memcache.set(cls.LAST_TIME_QUERIED, time.time())
            return all_posts
        else:
           return all_posts

    @classmethod
    def put_and_update_cache(cls, post):
        post.put()
        cls.get_all_order_by_date(True)

    def as_dict(self):
        time_fmt = '%c'
        d = {'title': self.title,
             'content': self.content,
             'created': self.created.strftime(time_fmt)}
        return d