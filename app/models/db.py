from flask_mongoengine import MongoEngine
#Creating the db object
db = MongoEngine()

# Database initialization function
def initialize_db(app):
    db.init_app(app)