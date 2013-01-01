from handlers.Handler import Handler
from entities.Post import Post

__author__ = 'ssav'

class Get_post(Handler):
    def get(self):
        id = self.request.path_info.replace('/blog/id/', '').replace('.json', '').replace('/', '')
        entry = Post.get_by_id(int(id))
        if self.format == 'html':
            self.render('post.html', entry=entry, id=id)
        else:
            self.render_json(entry.as_dict())
