import unittest
import requests


class Test_ya_folder(unittest.TestCase):
    def test_ya_folder(self):
        self.headers = {
            'Authorization': 'OAuth y0_Ag'
        }
        params = {'path': 'Image'}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        self.assertEqual(201, response.status_code)
