import web

urls = ('/', 'hello')
app = web.application(urls, globals())
render = web.template.render('templates/')


class hello:
    def GET(self):
        return render.hello()


application = app.wsgifunc()

