import json

from .baseCase import BaseTestCase



class GetArticlesTest(BaseTestCase):
    
    def test_empty_response(self):
        response = self.app.get('/articles')
        self.assertEqual(response.status_code, 200)
        
    def test_successful_storearticle(self):
        url={"url":"https://www.bbc.com/"}
        response = self.app.post('/articles', data=url)
        self.assertEqual(200, response.status_code)
        
    def test_successful_getarticles(self):
        url={"url":"https://www.bbc.com/"}
        response = self.app.post('/articles', data=url)
        response = self.app.get('/articles')
        # Then
        self.assertEqual(200, response.status_code)
     
        
   
