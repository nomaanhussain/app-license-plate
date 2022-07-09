import json
import os
import random
import sys
import unittest

sys.path.append(os.getcwd())
import api
from api import app_config


class MyTestCase(unittest.TestCase):

    

    def setUp(self):
        api.app.testing = True
        api.app.config.from_object(app_config.ProductionConfig)
        self.app = api.app.test_client()


    def test_home(self):
        response = self.app.get('/')
        # Make your assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'ok')


    def test_add_plate(self):
        plate_no = 'Z-ZZ' + str(random.randint(1000, 9999))
        response = self.app.post('/plate',json={
            "plate":plate_no
        })
        # Make your assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.text), {"response": "added"})


    def test_get_plates(self):
        response = self.app.get('/plate')
        # Make your assertions
        self.assertEqual(response.status_code, 200)


    def test_search_plate(self):
        response = self.app.get('/search-plate', query_string={'key': 'ZZZ5477', 'levenshtein': 0})
        # Make your assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.text), [{"plate": "ZZZ5477","timestamp": "2022-07-09T13:14:08Z"}])


if __name__ == '__main__':
    unittest.main()