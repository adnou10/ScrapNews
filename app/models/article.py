from .db import db

class Article(db.Document):
    headline = db.StringField(required=True)
    authors = db.ListField(db.StringField())
    summary=db.StringField()
    url = db.StringField(required=True)
    content = db.StringField()
    keywords = db.ListField(db.StringField())
    
    def __repr__(self):
        return '<article {}>'.format(self.headline)