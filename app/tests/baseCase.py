from unittest import TestCase

from app import app, models


class BaseTestCase(TestCase):
    """A base test case for flask-tracking."""
    
    def setUp(self):
        self.app = app.test_client()
        self.db = models.db.db.get_db()


    def tearDown(self):
        # Delete Database collections after the test is complete
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)