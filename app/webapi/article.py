# This file will contain our "views"
from flask import Response, request
from app.models.article import Article
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, DoesNotExist, ValidationError 

from .errors import SchemaValidationError, InternalServerError, ArticleNotExistsError


#Let's define our class ArticlesAPi 
class ArticlesApi(Resource):
    # to get all Articles
    def get(self):
        try:
            articles=Article.objects.to_json()
            return Response(articles,mimetype="application/json",status=200)
        except DoesNotExist:
            raise ArticleNotExistsError
        except Exception:
            raise InternalServerError
    
    
    #To add articles to the db
    def post(self):
        try:
            body = request.get_json()
            article = Article(**body).save()
            id = article.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError

#BK stands for by keyword
class ArticlesBKApi(Resource):
    #To get articles by keyword
    def get(self,keyword):
        try:
            articles=Article.objects(keywords=keyword).to_json()
            return Response(articles,mimetype="application/json",status=200)
        except DoesNotExist:
            raise ArticleNotExistsError
        
