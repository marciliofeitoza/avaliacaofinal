import os
import sys
import unittest
import requests
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, 'features/steps/json_scenarios')
sys.path.append(path_dir)

from json_utils import *

class Dashboard(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_dashboard(self):

        companie_id = get_id()
        auth = get_token()

        header = {'authorization': auth}
        response = requests.get(f'{self.url}/dashboard/{companie_id}', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        self.assertIn('journeys', json_data)
        self.assertEqual(type(json_data['journeys']), list)

        self.assertIn('journeys', json_data)
        self.assertEqual(type(json_data['journeys'][0]['id']), int)

        self.assertIn('journeys', json_data)
        self.assertEqual(type(json_data['journeys'][0]['sort_order']), int)

        self.assertIn('journeys', json_data)
        self.assertEqual(type(json_data['journeys'][0]['current']), bool)

        self.assertIn('journeys', json_data)
        self.assertEqual(type(json_data['journeys'][0]['open']), bool)

        self.assertIn('goals', json_data)
        self.assertEqual(type(json_data['goals']), dict)

        self.assertIn('goals', json_data)
        self.assertEqual(type(json_data['goals']['breakevenPoint']), float)

        self.assertIn('goals', json_data)
        self.assertEqual(type(json_data['goals']['salesGoal']), float)

        self.assertIn('goals', json_data)
        self.assertEqual(type(json_data['goals']['totalTaxForSale']), float)

        self.assertIn('goals', json_data)
        self.assertEqual(type(json_data['goals']['unitBP']), float)

        self.assertIn('progress', json_data)
        self.assertEqual(type(json_data['progress']), dict)

        self.assertIn('saleDevolutionInfo', json_data)
        self.assertEqual(type(json_data['saleDevolutionInfo']), dict)

        self.assertIn('formulas', json_data)
        self.assertEqual(type(json_data['formulas']), dict)

        self.assertIn('dre1', json_data)
        self.assertEqual(type(json_data['dre1']), dict)

        self.assertIn('dre2', json_data)
        self.assertEqual(type(json_data['dre2']), dict)
