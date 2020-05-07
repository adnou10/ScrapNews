#import modules
from flask import Flask
from config import Config

#Create app object
app = Flask(__name__)

#Configurate app object
app.config.from_object(Config)


#import our routes and models files
from app import routes, models, errors

#database initialization
models.db.initialize_db(app)


if __name__ == "__main__":
    app.run()
