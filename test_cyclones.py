'''A module for testing Cyclones'''
import unittest
from app import APP


class CyclonesTests(unittest.TestCase):
    '''Tests for the Cyclones application'''

    def setUp(self):
        '''Create a test client for the app'''
        self.app = APP.test_client()

    def test_valid_guid(self):
        '''test_valid_guid: a request for a valid GUID shall return 200 OK'''
        valid_guid = '05024756-765e-41a9-89d7-1407436d9a58'
        with self.app.get(f'/{valid_guid}') as res:
            self.assertEqual(res.status, '200 OK', f"Expected status code 200 OK for GUID {valid_guid}")

    def test_valid_guid_json(self):
        '''test_valid_guid_json: a request for the valid GUID shall return the correct JSON'''
        valid_guid = '05024756-765e-41a9-89d7-1407436d9a58'
        expected_json = {
            "guid": valid_guid,
            "latlong": "42.026111,-93.648333",
            "location": "Ames, IA, USA",
            "mascot": "Cy",
            "nickname": "Cyclones",
            "school": "Iowa State University"
        }
        with self.app.get(f'/{valid_guid}') as res:
            self.assertEqual(res.status, '200 OK', f"Expected status code 200 OK for GUID {valid_guid}")
            self.assertEqual(res.json, expected_json, f"Expected JSON {expected_json} for GUID {valid_guid}")

    def test_invalid_guid(self):
        '''test_invalid_guid: a request for an invalid GUID shall return 404 NOT FOUND'''
        invalid_guid = 'non-existent-guid'
        with self.app.get(f'/{invalid_guid}') as res:
            self.assertEqual(res.status, '404 NOT FOUND', f"Expected status code 404 NOT FOUND for GUID {invalid_guid}")
            self.assertIn('error', res.json, "Expected error message in the response JSON")


if __name__ == "__main__":
    unittest.main()
