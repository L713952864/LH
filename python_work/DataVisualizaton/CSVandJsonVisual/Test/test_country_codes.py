import unittest
from CSVandJsonVisual.country_codes import get_country_code


class CountryCodeTestCase(unittest.TestCase):
    """测试函数get_country_code"""
    def test_get_country_code(self):
        code = get_country_code('China')
        self.assertEqual(code, 'cn')