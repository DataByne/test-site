from flask import Blueprint

bp = Blueprint( 'auth', __name__ )

from blogsite.auth import routes
