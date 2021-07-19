# from flask_restful import  Resource
from flask.views import MethodView as _MethodView
from flask import (request, 
                render_template, 
                render_template_string, 
                abort
                )
from ..errors.misc import DataTypeMismatchError
from ..http.response import Response
from importlib import import_module
from asgiref.sync import async_to_sync
from inspect import iscoroutinefunction as is_async_func
import typing as t

class MethodView(_MethodView):
    """
    Navycut default view class to provide the interactive service and features.
    Simply import this class and extend it with your view class.
    for example:: 

        from navycut.urls import MethodView
        from navycut.http import JsonResponse

        class IndexView(MethodView):
            return JsonResponse(message="Salve Mundi!")
        #or
        class IndexView(MethodView):
            return self.render("index.html") # html templates must be present at app's specified template folder.
    """
    # available_methods = []

    def __init__(self, *wargs, **kwargs) -> None:
        super(MethodView, self).__init__(*wargs, **kwargs)

        self.req = self.request = request
        self.res = self.response = Response()
        self.context = dict()


    def get(self, *args, **kwargs):
        """simply override this function for get request"""
        abort(405)

    def put(self, *args, **kwargs):
        """simply override this function for put request"""
        abort(405)

    def post(self, *args, **kwargs):
        """simply override this function for post request"""
        abort(405)

    def delete(self, *args, **kwargs):
        """simply override this function for delete request"""
        abort(405)

    def head(self, *args, **kwargs):
        """simply override this function for head request"""
        abort(405)

    # def option(self, *args, **kwargs):
    #     """simply override this function for option request"""
    #     abort(405)


    def render(self, template_name_or_raw:str, *wargs:tuple, **context:t.Any):
        """
        The function to rend to html templates.
        :param template_name_or_raw:
            single template name or html raw string.
        :param wargs:
            only accept dictionary type value.
        :param context:
            provide the context for the html.

        example::

            class BlogView(MethodView):
                def get(self):
                    blogs = Blog.query.all()
                    return self.render("blog-list.html", blogs=blogs)
        """        
        if len(wargs) and not isinstance(wargs[0], dict): 
            raise DataTypeMismatchError(wargs[0], "template rendering", "dict")
        
        if len(wargs) and isinstance(wargs[0], dict):
            context.update(wargs[0])
        
        if isinstance(template_name_or_raw, str):
            if not template_name_or_raw.endswith(".html") and not template_name_or_raw.endswith(".htm"):
                return render_template_string(template_name_or_raw, **context)
            
            else: 
                return render_template(template_name_or_raw, **context)

    @classmethod
    def as_view(cls, name: str, *class_args: t.Any, **class_kwargs: t.Any):
        for method in list(cls.methods):
            if is_async_func(getattr(cls, method.lower())):
                setattr(cls, method.lower(), async_to_sync(getattr(cls, method.lower())))

        return super(MethodView, cls).as_view(name, *class_args, **class_kwargs)


class path:
    def __init__(self, url:str, views, name=None) -> None:
        self.url:str = "/"+url if not url.startswith('/') else url
        self.url = self.url+"/" if not self.url.endswith("/") else self.url
        self.views = views
        self.name:str = name or self.views.__name__
    
    def __repr__(self) -> str:
        return f"path <{self.url}>"

class url:
    def __init__(self, url:str, views, name=None) -> None:
        self.url = "/"+url if not url.startswith('/') else url
        self.url = self.url+"/" if not self.url.endswith("/") else self.url
        self.views = views
        self.name = name or self.views.__name__

    def __repr__(self) -> str:
        return f"url <{self.url}>"

class include:
    def __init__(self, 
                url_rule:str,
                url_module_name:str) -> None:

        self.url = "/"+url_rule if not url_rule.startswith('/') else url_rule
        self.url = self.url[:-1] if self.url.endswith("/") else self.url
        self.url_module = import_module(url_module_name)
        self.url_patterns = self.url_module.url_patterns

        for url_pattern in self.url_patterns:

            url_pattern.url = url_rule+url_pattern.url
            url_pattern.name = url_rule+url_pattern.name

    def __repr__(self) -> str:
        return f"include <{self.url}>"