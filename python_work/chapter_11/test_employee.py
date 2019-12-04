"""关于Employee类的测试用例"""
import unittest
from chapter_11.employee import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        """创建一个实例并设置属性，供测试使用"""
        self.person = Employee('Lily', 'Albert', 43000)

    def test_give_default_raise(self):
        self.person.give_raise()
        self.assertEqual(48000, self.person.income)

    def test_give_custom_raise(self):
        self.person.give_raise(10000)
        self.assertEqual(53000, self.person.income)