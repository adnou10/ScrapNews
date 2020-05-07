import json

from .BaseCase import BaseCase



class ApiTest(BaseCase):
    
    def test_empty_response(self):
        response = self.app.get('/api/articles/')
        self.assertEqual(response.status_code, 200)

    def test_successful_post(self):
        payload = json.dumps({
            "authors":["author1","author2"],
            "content":"content test",
            "summary":"test sum",
            "url":"www.test.com",           
            "headline":"headline test",
            "keywords":["keyword","corona","test"]
            })
        response = self.app.post('/api/articles/', headers={"Content-Type": "application/json"}, data=payload)
        response = self.app.get('/api/articles/corona')
        # Then
        self.assertEqual(200, response.status_code)
