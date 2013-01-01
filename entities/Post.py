from google.appengine.ext import db
from google.appengine.api import memcache
import time

__author__ = 'ssav'



class Post(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    ALL_POSTS = 'all_posts'
    LAST_TIME_QUERIED_ALL_POSTS = 'last time queried all posts'
    POST = 'post#:'
    LAST_TIME_QUERIED_POST = 'last time queried post#'

    @classmethod
    def get_all_order_by_date(cls, update_cache = False):
        all_posts = memcache.get(cls.ALL_POSTS)
        if update_cache or all_posts is None:
            all_posts = Post.gql('ORDER BY created DESC')
            memcache.set(cls.ALL_POSTS, all_posts)
            memcache.set(cls.LAST_TIME_QUERIED_ALL_POSTS, time.time())
        return all_posts

    @classmethod
    def put_and_update_cache(cls, post):
        post.put()
        cls.get_all_order_by_date(True)

    @classmethod
    def get_by_id_and_update_cache(cls, id):
        post = memcache.get(cls.POST + str(id))
        if post is None:
            post = Post.get_by_id(id)
            memcache.set(cls.POST + str(id), post)
            memcache.set(cls.LAST_TIME_QUERIED_POST + str(id), time.time())
        return post

    def as_dict(self):
        time_fmt = '%c'
        d = {'title': self.title,
             'content': self.content,
             'created': self.created.strftime(time_fmt)}
        return d