import unittest
from app import app  # Import your Flask app
from datetime import datetime
import random

class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Backend is Running', response.data)

    def test_get_battery_data(self):
        response = self.app.get('/battery-data')
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.get_json())

    def test_post_battery_data(self):
        status='No data'
        soc=random.randint(0,100)
        soh=random.randint(0,100)
        if (soh>=0  and soh<40) :
            status='Poor Battery health'
        elif (soh>=40 and soh<60):
            status='Average Battery Health'
        elif(soh>=60 and soh<=100):
            status='Good Battery Health'
        else:
            status='No data'
        payload = {
            "soc": soc,
            "soh": soh,
            "timestamp": status,
        }
        response = self.app.post('/battery-data', json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn('success', response.get_json().get('status'))

if __name__ == "__main__":
    unittest.main()
