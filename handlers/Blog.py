from handlers.Handler import Handler
from entities.Post import Post
from google.appengine.api import memcache
import time

__author__ = 'ssav'

class Blog(Handler):
    def get(self):
        entries = Post.get_all_order_by_date()
        if self.format == 'html':
            self.render('blog.html', entries=entries, seconds_ago='%f' % (time.time() - memcache.get(Post.LAST_TIME_QUERIED_ALL_POSTS)))
        else:
            return self.render_json([e.as_dict() for e in entries])

