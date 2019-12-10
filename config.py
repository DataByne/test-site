import os
from dotenv import load_dotenv

basedir = os.path.abspath( os.path.dirname( __file__ ) )
load_dotenv( os.path.join( basedir, '.env' ) )

class BaseConfig( object ):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'fr']


class BuildConfig( BaseConfig ):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    

class TestConfig( BaseConfig ):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
