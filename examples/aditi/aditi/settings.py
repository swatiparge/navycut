from navycut.utils import path

# defining the default import name for flask:
IMPORT_NAME = __name__

#defining the actual project name:
PROJECT_NAME = "aditi"


#defining the base directory
BASE_DIR = path.abspath(__file__).parent.parent

TEMPLATE_DIR = BASE_DIR / "templates"

#app debug state:
DEBUG = True

#defining the base database configuration.
DATABASE = dict(
    engine = "navycut.orm.sqla.engine.sqlite3",
    creds = dict(
        host = None,
        username = None,
        password = None,
        database = BASE_DIR / "navycut.sqlite3"
    )
)

#defining the navycut app secret key
SECRET_KEY = r"f7>Rn2eJli}>kVr7Hj@6^$&2P35Bx^>C^}FsOKG94SER!lwgtx[Wa" #should generate randomly at the time of creation.


#available installed app add here to bloom.
INSTALLED_APPS = [ # should change to first_app to get the app.
    "navycut.orm.sqla",
    "navycut.contrib.cors",
    "navycut.contrib.auth",
    "navycut.contrib.mail",
    "navycut.contrib.admin",
    "navycut.helpers.upload_server",
    "aniket",
    "sarkar",
    "kolkata",
    "plassey"
    #"first_app.sister.FirstappSister", 
]

MIDDLEWARE = [
    "navycut.middleware.ipfilter.IPFilterMiddleware",
]

ALLOWED_HOST = [ # 
    '127.0.0.1', 
]

# Email SMTP Configuration
MAIL_USING_SMTP = False

SMTP_CONFIGURATION = dict(
    host = None,
    port = None,
    username = None,
    password = None,
    is_using_ssl = None,
    is_using_tls = None,
    options = None
)


EXTRA_ARGS = None

CORS_RESOURCES = {}