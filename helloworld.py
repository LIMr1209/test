#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.gen as gen
import time

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class NonBlockingHandler(tornado.web.RequestHandler):

    @gen.coroutine  # 异步非堵塞
    def get(self):
        print(1)
        yield tornado.gen.sleep(5)
        print(2)
        self.write('"Hello, world"')


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('index')


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        print(1)
        time.sleep(5)
        print(2)
        self.write('test')


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/index", IndexHandler),
        (r"/nonblocking", NonBlockingHandler),
        (r"/test", TestHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
