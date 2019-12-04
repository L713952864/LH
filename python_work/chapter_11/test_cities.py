import unittest
from chapter_11.city_functions import get_city_country


class CityTestCase(unittest.TestCase):
    """测试city_function.py
        编写一系列方法对函数行为的不同方面进行测试
    """

    def test_city_country(self):
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        city_country = get_city_country('santiago', 'chile', 5000000)
        self.assertEqual((city_country, 'Santiago, Chile - population 5000000'))


unittest.main()