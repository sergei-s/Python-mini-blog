import webapp2
from handlers.Blog import Blog
from handlers.Get_post import Get_post
from handlers.New_entry import New_entry
from handlers.Signup import Signup
from handlers.Welcome import Welcome


app = webapp2.WSGIApplication([('/blog', Blog),
                               ('/blog/newpost', New_entry),
                               ('/blog/id/.*', Get_post),
                               ('/blog/signup', Signup),
                               ('/blog/welcome', Welcome)],
                               debug=True)
