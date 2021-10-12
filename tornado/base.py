import tornado.ioloop
from tornado.escape import json_decode
from tornado.web import RequestHandler, Application, url, RedirectHandler

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user_id = self.get_secure_cookie("user")
        if not user_id: return None
        return "张三"

    def get_user_locale(self):
        if "locale" not in self.current_user.prefs:
            # Use the Accept-Language header
            return None
        return self.current_user.prefs["locale"]


class MainHandler(BaseHandler):
    def initialize(self):
        self.supported_path = ['path_a', 'path_b', 'path_c']

    def prepare(self):
        action = self.request.path.split('/')[-1]
        if action not in self.supported_path:
            self.send_error(400)

        if self.request.headers['Content-Type'] == 'application/x-json':
            self.args = json_decode(self.request.body)

    # def get(self):
        # self.write('<a href="%s">link to story 1</a>' %
        #            self.reverse_url("story", "1"))
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("template.html", title="My title", items=items)


class StoryHandler(RequestHandler):
    # def initialize(self, db):
    #     self.db = db

    def get(self, story_id):
        self.write("this is story %s" % story_id)


def make_app():
    return Application([
        url(r"/", MainHandler),
        url(r"/story/([0-9]+)", StoryHandler, name="story")
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
