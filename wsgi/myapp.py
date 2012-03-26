import web

urls = (
  '/', 'hello')


class hello:
    def GET(self):
        return 'Hello, web!'


app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()

