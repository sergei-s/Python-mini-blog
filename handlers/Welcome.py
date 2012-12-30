from handlers.Handler import Handler

__author__ = 'ssav'

class Welcome(Handler):
    def get(self):
        username = self.read_secure_cookie('name')
        if username:
            self.render('welcome.html', user = username)
        else:
            self.redirect('/signup')