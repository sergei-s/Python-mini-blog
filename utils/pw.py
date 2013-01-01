import random
import string
import hashlib

__author__ = 'ssav'

def make_salt():
    choices = string.letters + string.digits
    return ''.join(random.choice(choices) for x in range(5))


def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)


def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    return h == make_pw_hash(name, pw, salt)
