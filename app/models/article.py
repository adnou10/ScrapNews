from .db import db

# This the model of our documents
class Article(db.Document):
    headline = db.StringField(required=True)
    authors = db.ListField(db.StringField())
    summary=db.StringField()
    url = db.StringField(required=True)
    content = db.StringField()
    keywords = db.ListField(db.StringField())
    
    #To print objects of our class
    def __repr__(self):
        return '<article {}>'.format(self.headline)