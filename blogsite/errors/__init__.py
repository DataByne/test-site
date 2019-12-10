from flask import Blueprint

bp = Blueprint( 'errors', __name__ )

from blogsite.errors import handlers
