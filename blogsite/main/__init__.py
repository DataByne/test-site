from flask import Blueprint

bp = Blueprint( 'main', __name__ )

from blogsite.main import routes
