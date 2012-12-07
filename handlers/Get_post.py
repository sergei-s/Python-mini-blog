from handlers.Handler import Handler
from entities.Post import Post

__author__ = 'ssav'

class Get_post(Handler):
    def get(self):
        path = self.request.path_info
        path = path.replace('/blog/id/', '')
        entry = Post.get_by_id(int(path))
        self.render('post.html', entry=entry, path=path)
