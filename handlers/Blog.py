from handlers.Handler import Handler
from entities.Post import Post

__author__ = 'ssav'

class Blog(Handler):
    def get(self):
        entries = Post.gql('ORDER BY created DESC')
        self.render('blog.html', entries=entries)