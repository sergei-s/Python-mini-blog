import webapp2
from handlers.Flush import Flush
from handlers.Blog import Blog
from handlers.Get_post import Get_post
from handlers.Login import Login
from handlers.Logout import Logout
from handlers.New_entry import New_entry
from handlers.Signup import Signup
from handlers.Welcome import Welcome

app = webapp2.WSGIApplication([('/blog(?:.json)?/?', Blog),
                               ('/blog/newpost/?', New_entry),
                               ('/blog/id/.*/?(?:.json)?', Get_post),
                               ('/blog/signup/?', Signup),
                               ('/blog/welcome/?', Welcome),
                               ('/blog/login/?', Login),
                               ('/blog/logout/?', Logout),
                               ('/blog/flush/?', Flush)],
                               debug=True)
