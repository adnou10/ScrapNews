# This file will contain our "views"
from flask import Response, request
from app.models.article import Article
from flask_restful import Resource



#Let's define our class ArticlesAPi 
#class ArticlesApi(Resource):
    # to get all Articles
    #def get(self):
    #        articles=Article.objects.to_json()
    #        return Response(articles,mimetype="application/json",status=200)
        
    
    
    #To add articles to the db
    #def post(self):
    #    body = request.get_json()
    #    article = Article(**body).save()
    #    id = article.id
    #    return {'id': str(id)}, 200

#BK stands for by keyword
class ArticlesBKApi(Resource):
    #To get articles by keyword
    def get(self,keyword):
            articles=Article.objects.get(keywords=keyword).to_json()
            return Response(articles,mimetype="application/json",status=200)
