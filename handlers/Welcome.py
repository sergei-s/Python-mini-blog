from handlers.Handler import Handler

__author__ = 'ssav'

class Welcome(Handler):
    def get(self):
        self.render('welcome.html', user = self.request.cookies.get('name'))