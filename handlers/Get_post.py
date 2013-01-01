from handlers.Handler import Handler
from entities.Post import Post
from google.appengine.api import memcache
import time

__author__ = 'ssav'

class Get_post(Handler):
    def get(self):
        id = self.request.path_info.replace('/blog/id/', '').replace('.json', '').replace('/', '')
        entry = Post.get_by_id_and_update_cache(int(id))
        if self.format == 'html':
            self.render('post.html', entry=entry, id=id, seconds_ago = '%f' % (time.time() - memcache.get(Post.LAST_TIME_QUERIED_POST + id)))
        else:
            self.render_json(entry.as_dict())
