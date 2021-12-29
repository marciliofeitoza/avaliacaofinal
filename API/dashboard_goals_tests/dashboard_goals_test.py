import os
import sys
import unittest
import requests
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, 'features/steps/json_scenarios')
sys.path.append(path_dir)

from json_utils import *

class DashboardGoals(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_dashboardGoals(self):

        companies_id = get_id()
        auth = get_token()

        header = {'authorization': auth}
        response = requests.get(f'{self.url}/dashboard/goals/{companies_id}', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.text)

        self.assertIn('breakevenPoint', json_data)
        self.assertEqual(type(json_data['breakevenPoint']), float)

        self.assertIn('salesGoal', json_data)
        self.assertEqual(type(json_data['salesGoal']), float)

        self.assertIn('totalTaxForSale', json_data)
        self.assertEqual(type(json_data['totalTaxForSale']), float)

        self.assertIn('unitBP', json_data)
        self.assertEqual(type(json_data['unitBP']), float)

        self.assertIn('unitSG', json_data)
        self.assertEqual(type(json_data['unitSG']), float)
