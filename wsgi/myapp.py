import web

urls = ('/', 'hello')


class hello:
    def GET(self):
        render = web.template.render('templates')
        return render.hello()


app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()

