from entities.User import User
from handlers.Handler import Handler
import pw

__author__ = 'ssav'

class Login(Handler):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        user = User.gql('WHERE username = :username', username=username)
        if user.count() == 0:
            self.display_error()
        else:
            if pw.valid_pw(username, password, user[0].password):
                self.set_secure_cookie('name', str(username))
                self.redirect('/blog/welcome')
            else:
                self.display_error()

    def display_error(self):
        error = 'Not valid'
        self.render('login.html', error = error)