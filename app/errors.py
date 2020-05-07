class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class ArticleNotExistsError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields ",
         "status": 400
     },
     "ArticleNotExistsError": {
         "message": "Articles with given keyword doesn't exists",
         "status": 400
     }
}