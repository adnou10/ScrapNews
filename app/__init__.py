#import modules
from flask import Flask
from config import Config
from flask_restful import Api

#Create app object
app = Flask(__name__)



#Configurate app object
app.config.from_object(Config)



#import our routes and models files
from app import routes, models
from app.webapi import endp, errors

#Create api object
api = Api(app,errors=errors)
#database initialization
models.db.initialize_db(app)

#initialize api routes
endp.initialize_routes(api)


if __name__ == "__main__":
    app.run()
