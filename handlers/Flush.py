from handlers.Handler import Handler
from google.appengine.api import memcache

__author__ = 'ssav'

class Flush(Handler):
    def get(self):
        memcache.flush_all()
        self.redirect('/blog')
