import web
# from view import render
from web import form

urls = (
    "/(.*)", "index"
)

login = web.form.Form(
    form.Textbox('username'),
    form.Password('Password'),
    form.Button('Login'),
)


class index:
    def GET(self, name):

        render = web.template.render("templates/")
        #		name = web.input(name=None)
        #		name = 'fangkuan'
        return render.welcome(name, login)


class add:
    def post(self):
        #i = web.input()
        #f = login()
        data = web.data()
        #print data
        render = web.template.render("templates/")
        #return render.LoginSuccess()
        raise web.seeother("/"+'templates/LginSuccess.html')


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
