from entities.User import User
from handlers.Handler import Handler
import pw

__author__ = 'ssav'

class Signup(Handler):
    def get(self):
        self.render('signup.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        username_error = ''
        password_error = ''
        verify_error = ''
        email_error = ''
        is_valid = True
        if password != verify:
            verify_error = 'Password and verify do not match'
            is_valid = False
        if not username:
            username_error = 'Fill username'
            is_valid = False
        if not password:
            password_error = 'Fill password'
            is_valid = False
        if not verify:
            verify_error = 'Fill verify'
            is_valid = False
        if email:
            user_by_email_count = User.gql('WHERE email = :email', email=email).count()
            if user_by_email_count == 1:
                email_error = 'Email already exists'
                is_valid = False
        user_by_name_count = User.gql('WHERE username = :username', username = username).count()

        if user_by_name_count == 1:
            username_error = 'User already exists'
            is_valid = False

        if is_valid:
            user = User(username=username, password=pw.make_pw_hash(username, password), email=email)
            user.put()
            self.response.headers.add_header('Set-Cookie', 'name=%s; Path=/' % str(username))
            self.redirect('/blog/welcome')
        else:
            self.render('signup.html',
                username_error=username_error,
                password_error=password_error,
                verify_error=verify_error,
                email_error=email_error,
                username=username,
                email=email)
