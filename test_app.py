'''A module for testing'''
import unittest
from app import APP


class Tests(unittest.TestCase):
    '''Basic tests for the application'''

    def setUp(self):
        '''Create a test client for the app'''
        self.app = APP.test_client()

    def test_200(self):
        '''test_200: a request for / shall return 200 OK'''
        with self.app.get('/') as res:
            self.assertEqual(res.status, '200 OK', "Expected status code 200 OK")

    def test_404(self):
        '''test_404: a request for null shall return 404 NOT FOUND'''
        with self.app.get('/null') as res:
            self.assertEqual(res.status, '404 NOT FOUND', "Expected status code 404 NOT FOUND")


if __name__ == "__main__":
    unittest.main()
