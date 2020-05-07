from .article import ArticlesBKApi , ArticlesApi

def initialize_routes(api):
    api.add_resource(ArticlesApi, '/api/articles/')
    api.add_resource(ArticlesBKApi, '/api/articles/<keyword>')
