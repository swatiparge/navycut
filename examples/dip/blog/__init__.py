"""
Do not change anything if you dont have enough knowledge 
about how to handle it, otherwise it may mess with the server.
"""

from navycut.core import AppSister
from os.path import abspath
from pathlib import Path
from .urls import url_patterns

__basedir__ = Path(abspath(__file__)).parent

_config__dict = {
    "import_name" : "blog",
    "name" : __name__,
    "template_folder" : __basedir__ / "templates",
    "static_folder" : __basedir__ / "static",
    "static_url_path" : "/blog/static/",
    "url_prefix" : "/blog",
}

app = AppSister(_config__dict)

app.add_url_pattern(url_patterns)
app.import_app_features()