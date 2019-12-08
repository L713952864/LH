from API.python_repos import get_status_code
import unittest
import requests

URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)


class PythonReposTestCase(unittest.TestCase):
    def test_status_code(self):
        code = get_status_code(r)
        self.assertEqual(code, 200)