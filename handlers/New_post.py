from handlers.Handler import Handler
from entities.Post import Post
from google.appengine.api import memcache
import time

__author__ = 'ssav'

class New_entry(Handler):
    def get(self):
        username = self.get_username()
        if username:
            self.render('new_post.html')
        else:
            self.redirect('/blog/login')

    def post(self):
        title = self.request.get('subject')
        content = self.request.get('content')
        if title and content:
            e = Post(title=title, content=content)
            Post.put_and_update_cache(e)
            self.redirect('/blog/id/' + str(e.key().id()))
        else:
            error = 'Fill both title and content'
            self.render('new_post.html', title=title, content=content, error=error)