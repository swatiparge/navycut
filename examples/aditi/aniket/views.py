from navycut.contrib.auth import login_required
from .models import Blog, ExtraUser
from navycut.contrib.mail import send_mail
from navycut.typing import *
from navycut.urls import MethodView
from navycut.contrib.forms import ModelForm


class HelloView(MethodView):
    async def get(self):
        # print (list(self.methods))
        return "hello from index page"
        

    async def post(self):
        return "request from post page"


async def homepage(req:ncRequest, res:ncResponse):
    return res.json(dict(req.headers))


# @login_required
# @group_required("super_admin")
def another_page(req, res):
    # r = Request(request.environ)
    # print (req.user.username)
    # return res.status(201).json(name=req.user.name)
    return res.end(200)
    # return res \
    #     .set_status(404)\
    #         .render("<h1>Hello {{name}}</h1>", name="Aniket")

@login_required
def aditi(req, res):
    return res.json(username=req.user.username)

def send_email(req, res):
    send_mail("this is subject", "this is message", recipient_list=['aniketsarkar@yahoo.com'], html_message="<h1>this is html text</h1>")
    return res.json(mesage="email sended successfully.")

def get_blog(req, res, id):
    # author = Author.query.get(id)
    blog =Blog.query.get(id)
    print (blog.__table__)
    # print (blog.author)
    return res.json(blog)

class BlogForm(ModelForm):
    model = ExtraUser


def blogger(req, res):
    blog = ExtraUser()
    success = False
    blogform = BlogForm()

    if req.method == "POST":
        
        form = blogform(req.form, blog)
        if form.validate():
            form.populate_obj(blog)
            blog.save()
            success = True
    else:
        form = blogform(instance=blog)

    return res.render("create.html", form=form, success=success)