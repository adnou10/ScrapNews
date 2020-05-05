import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "#d#JCqTTW\nilK\\7m\y0bp#\tj~#H"
    MONGODB_SETTINGS = {
    'host': 'mongodb+srv://testuser:0000@articles-ce4va.mongodb.net/test?retryWrites=true&w=majority'
}