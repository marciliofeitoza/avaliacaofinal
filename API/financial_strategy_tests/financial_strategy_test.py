import os
import sys
import unittest
import requests
import json

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, 'features/steps/json_scenarios')
sys.path.append(path_dir)

from json_utils import *

class FinancialStrategy(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_financialStrategy(self):

        companies_id = get_id()
        auth = get_token()

        header = {'authorization': auth}
        response = requests.get(f'{self.url}/financial-strategy/{companies_id}', headers=header)
        assert response.status_code == 200
