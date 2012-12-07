from handlers.Handler import Handler
from entities.Post import Post

__author__ = 'ssav'

class New_entry(Handler):
    def get(self):
        self.render('new_entry.html')

    def post(self):
        title = self.request.get('subject')
        content = self.request.get('content')
        if title and content:
            e = Post(title=title, content=content)
            e.put()
            self.redirect('/blog/id/' + str(e.key().id()))
        else:
            error = 'Fill both title and content'
            self.render('new_entry.html', title=title, content=content, error=error)