from entities.User import User
from handlers.Handler import Handler

__author__ = 'ssav'

class Signup(Handler):
    def get(self):
        self.render('signup.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username = username,
            email = email)

        is_valid = True
        if password != verify:
            params['verify_error'] = 'Password and verify do not match'
            is_valid = False
        if not username:
            params['username_error'] = 'Fill username'
            is_valid = False
        if not password:
            params['password_error'] = 'Fill password'
            is_valid = False
        if not verify:
            params['verify_error'] = 'Fill verify'
            is_valid = False
        if email and User.get_by_email(email).count() == 1:
            params['email_error'] = 'Email already exists'
            is_valid = False

        if User.get_by_name(username).count() == 1:
            params['username_error'] = 'User already exists'
            is_valid = False

        if is_valid:
            User.register(username, password, email)
            self.set_secure_cookie('name', str(username))
            self.redirect('/blog/welcome')
        else:
            self.render('signup.html', **params)
