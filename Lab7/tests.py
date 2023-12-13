import unittest
from unittest.mock import patch
from io import StringIO

from prettytable import PrettyTable

from Classes.lab_7.RequestsAPI import RequestsAPI


class TestRequestsAPI(unittest.TestCase):

    def setUp(self):
        self.site = 'https://jsonplaceholder.typicode.com/users'
        self.params = {}
        self.response = RequestsAPI(site=self.site, params=self.params)

    def test_get_headers(self):
        headers = self.response.get_headers()
        self.assertIsInstance(list(headers), list)
        self.assertTrue(all(isinstance(header, str) for header in headers))

    def test_get_table(self):
        table = self.response.get_table()
        self.assertIsInstance(table, PrettyTable)

    def test_get_custom_headers(self):
        custom_headers = [{'header': 'name', 'color': 'RED', 'font': 'bold'}]
        headers = self.response.get_custom_headers(custom_headers)
        self.assertEqual(headers, ['name'])

    def test_get_custom_table(self):
        custom_headers = [{'header': 'name', 'color': 'RED', 'font': 'bold'}]
        table, data = self.response.get_custom_table(custom_headers)
        self.assertIsInstance(table, PrettyTable)
        self.assertIsInstance(data, list)

    def test_set_custom_headers(self):
        custom_headers = [{'header': 'name', 'color': 'RED', 'font': 'bold'}]
        new_headers = self.response.set_custom_headers(custom_headers, self.response.data)
        expected_headers = ['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company']

        # Set style only for the specified custom header
        expected_styled_headers = [self.response.set_style(header, 'RED', 'bold') if header == 'name' else header for
                                   header in expected_headers]

        self.assertEqual(new_headers, expected_styled_headers)

    def test_save_to_json(self):
        filename = 'test_json_output'
        self.response.save_to_json(filename)
        # Add assertions to check if the file is created and contains expected data

    def test_save_to_csv(self):
        filename = 'test_csv_output'
        self.response.save_to_csv(filename)
        # Add assertions to check if the file is created and contains expected data

    def test_save_to_txt(self):
        filename = 'test_txt_output'
        self.response.save_to_txt(filename)
        # Add assertions to check if the file is created and contains expected data

if __name__ == '__main__':
    unittest.main()
