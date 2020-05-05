#import libraries
import os

#configuration class that holds all neccessary configs
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "#d#JCqTTW\nilK\\7m\y0bp#\tj~#H"
   
    #Our Mongodb settings / MongoDb Atlas URI
    MONGODB_SETTINGS = {
    'host': 'mongodb+srv://testuser:0000@articles-ce4va.mongodb.net/test?retryWrites=true&w=majority'
}