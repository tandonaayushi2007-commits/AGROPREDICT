"""
AgroPredict - Automated Test Suite
Tests model loading, inference accuracy, Flask routes, input validation, and error handling.
"""

import unittest
import json
import os
import pandas as pd
import numpy as np

from app import app, load_trained_model, FEATURE_ORDER, FIELD_VALIDATION_RULES
from crop_data import CROP_DATABASE, get_crop_info


class TestAgroPredict(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configure test client
        app.config['TESTING'] = True
        cls.client = app.test_client()
        load_trained_model()

    def test_01_index_route(self):
        """Test home route returns HTML."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'AgroPredict', response.data)
        self.assertIn(b'Predict Recommended Crop', response.data)

    def test_02_health_route(self):
        """Test healthcheck endpoint."""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')
        self.assertTrue(data['model_loaded'])
        self.assertEqual(data['crops_supported'], 22)

    def test_03_presets_route(self):
        """Test presets endpoint returns valid test presets."""
        response = self.client.get('/api/presets')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertGreaterEqual(len(data['presets']), 4)

    def test_04_crops_catalog(self):
        """Test crops catalog endpoint returns all 22 crops."""
        response = self.client.get('/api/crops')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['total_crops'], 22)
        self.assertIn('rice', data['crops'])
        self.assertIn('coffee', data['crops'])
        self.assertIn('cotton', data['crops'])

    def test_05_predict_rice(self):
        """Test real prediction on typical Rice conditions."""
        payload = {
            "N": 90,
            "P": 42,
            "K": 43,
            "temperature": 20.88,
            "humidity": 82.0,
            "ph": 6.5,
            "rainfall": 202.9
        }
        response = self.client.post('/predict',
                                   data=json.dumps(payload),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['predicted_crop'], 'rice')
        self.assertGreater(data['confidence'], 80.0)
        self.assertEqual(data['crop_info']['name'], 'Rice')
        self.assertIn('farming_tips', data['crop_info'])

    def test_06_predict_coffee(self):
        """Test real prediction on typical Coffee conditions."""
        payload = {
            "N": 100,
            "P": 25,
            "K": 30,
            "temperature": 26.0,
            "humidity": 55.0,
            "ph": 6.7,
            "rainfall": 170.0
        }
        response = self.client.post('/predict',
                                   data=json.dumps(payload),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['predicted_crop'], 'coffee')

    def test_07_validation_missing_parameter(self):
        """Test validation error when required parameter is missing."""
        payload = {
            "N": 90,
            "P": 42,
            "K": 43,
            "temperature": 20.88,
            # humidity missing
            "ph": 6.5,
            "rainfall": 202.9
        }
        response = self.client.post('/predict',
                                   data=json.dumps(payload),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['status'], 'error')
        self.assertIn('humidity', data['errors'])

    def test_08_validation_out_of_bounds(self):
        """Test validation error when parameter is out of bounds."""
        payload = {
            "N": 90,
            "P": 42,
            "K": 43,
            "temperature": 20.88,
            "humidity": 150.0,  # Invalid humidity > 100%
            "ph": 6.5,
            "rainfall": 202.9
        }
        response = self.client.post('/predict',
                                   data=json.dumps(payload),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['status'], 'error')
        self.assertIn('humidity', data['errors'])

    def test_09_validation_non_numeric(self):
        """Test validation error when string is entered instead of number."""
        payload = {
            "N": "invalid_num",
            "P": 42,
            "K": 43,
            "temperature": 20.88,
            "humidity": 82.0,
            "ph": 6.5,
            "rainfall": 202.9
        }
        response = self.client.post('/predict',
                                   data=json.dumps(payload),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['status'], 'error')
        self.assertIn('N', data['errors'])

    def test_10_about_model_content(self):
        """Test About the Model section exists with required content."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        html = response.data.decode('utf-8')
        
        self.assertIn('About the Model', html)
        self.assertIn('AgroPredict uses a Machine Learning-based Random Forest Classifier to recommend the most suitable crop based on soil and environmental conditions.', html)
        self.assertIn('The model analyzes seven important parameters: Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, soil pH, and rainfall.', html)
        self.assertIn('It is trained on the Crop Recommendation dataset containing different crop categories and their suitable growing conditions.', html)
        self.assertIn('The system is designed to assist farmers and users in making more informed crop selection decisions.', html)

    def test_11_footer_developer_attribution(self):
        """Test professional footer displays project title and developers with IDs."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        html = response.data.decode('utf-8')
        
        self.assertIn('AI-Based Agriculture Crop Recommendation System', html)
        self.assertIn('Developed by:', html)
        self.assertIn('Aayushi Tandon', html)
        self.assertIn('72511209', html)
        self.assertIn('Amritpal', html)
        self.assertIn('72512012', html)


if __name__ == '__main__':
    unittest.main()
