from entities.User import User
from handlers.Handler import Handler
from utils import pw

__author__ = 'ssav'

class Login(Handler):
    def get(self):
        username_error = ''
        self.render('login.html', username_error = username_error)

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        user = User.get_by_name(username)
        if user.count() == 0:
            self.display_error(username)
        else:
            if pw.valid_pw(username, password, user[0].password):
                self.set_secure_cookie('name', str(username))
                self.redirect('/blog/welcome')
            else:
                self.display_error(username)

    def display_error(self, username):
        error = 'Not valid'
        self.render('login.html', error = error, username_error = username)