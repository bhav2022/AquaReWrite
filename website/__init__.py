import os.path
import pathlib

from flask import Flask, session, abort
from google_auth_oauthlib.flow import Flow

ALLOWED_EXTENSIONS = set(['pdf', 'doc', 'docx'])

def allowed_files(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

GOOGLE_CLIENT_ID = "554282819719-c1v34tmkuvkule51llbtfp8u99ikhoqj.apps.googleusercontent.com"
client_secret_files = os.path.join(pathlib.Path(__file__).parent, "cred.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secret_files,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email",
            "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'wishlist'
    app.secret_key = 'wishlist'
    app.config['app_name'] = 'AquaReWrite'

    from .views import views
    from .auth import auth
    from .posts import posts
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(posts, url_prefix='/posts')

    return app

