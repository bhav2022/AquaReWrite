from flask import Flask, blueprints
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "users.db"

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'wishlist'
  app.secret_key = 'wishlist'
  app.config['app_name'] = 'AquaMainWeb'
  app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
  db.init_app(app)

  from .views import views
  from .auth import auth
  from .posts import posts
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  app.register_blueprint(posts, url_prefix='/posts')

  from .models import User


  with app.app_context():
      db.create_all()

  login_manager = LoginManager(app)
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
      return User.query.get(int(id))

  return app
