from handlers.Handler import Handler

__author__ = 'ssav'

class Logout(Handler):
    def get(self):
        self.set_secure_cookie('name', '')
        self.redirect('/blog')