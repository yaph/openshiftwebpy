import web

render = web.template.render('templates/')
urls = ('/', 'hello')


class hello:
    def GET(self):
        return render.hello


app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()

