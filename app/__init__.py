from flask import Flask
# from flask_bootstrap import Bootstrap
from config import config_options

# bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    # bootstrap.init_app(app)

    # Adding the main blue print
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # user's bluePrint
    from .usersAuth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')

     # Admin bluePrint
    from .adminAuth import admin as admin_blueprint
    app.register_blueprint(admin_blueprint,url_prefix='/admin')
    
    return app