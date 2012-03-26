import web

urls = ('/', 'hello')


class hello:
    def GET(self):
        render = web.template.render('templates')
        print render.hello()


app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()

