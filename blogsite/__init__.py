import os
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_babel import Babel, lazy_gettext as _l
from config import BuildConfig

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
mail = Mail()
bootstrap = Bootstrap()
babel = Babel()

def create_app( configClass = BuildConfig ):
	app = Flask( __name__ )
	app.config.from_object( configClass )

	db.init_app( app )
	migrate.init_app( app, db )
	login.init_app( app )
	mail.init_app( app )
	bootstrap.init_app( app )
	babel.init_app( app )

	# from blogsite.errors import bp as errors_bp
	# app.register_blueprint( errors_bp )

	from blogsite.auth import bp as auth_bp
	app.register_blueprint( auth_bp )

	from blogsite.main import bp as main_bp
	app.register_blueprint( main_bp )

	# from blogsite.project import bp as project_bp
	# app.register_blueprint( project_bp )

	# if not app.testing:
		# if app.config['MAIL_SERVER']:
		# 	auth = None
		# 	if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
		# 		auth = (app.config['MAIL_USERNAME'],
		# 				app.config['MAIL_PASSWORD'])
		# 	secure = None
		# 	if app.config['MAIL_USE_TLS']:
		# 		secure = ()
		# 	mail_handler = SMTPHandler(
		# 		mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
		# 		fromaddr='no-reply@' + app.config['MAIL_SERVER'],
		# 		toaddrs=app.config['ADMINS'], subject='Microblog Failure',
		# 		credentials=auth, secure=secure)
		# 	mail_handler.setLevel(logging.ERROR)
			# app.logger.addHandler(mail_handler)

	return app
	
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])

from blogsite import models
