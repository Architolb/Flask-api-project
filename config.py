# file structure and organization
import os

#setup classes
basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    """
    setting configuration variables that tell flask app how to run
    """

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
