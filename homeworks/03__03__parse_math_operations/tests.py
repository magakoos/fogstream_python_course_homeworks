# coding=utf8

import unittest
from main import use_operation, parse_math_string, unbracket


class SeimpleTest(unittest.TestCase):

    def test_use_operation_add(self):
        self.assertEqual(use_operation('2', '+', '3'), 5)

    def test_use_operation_sun(self):
        self.assertEqual(use_operation('10', '-', '3'), 7)

    def test_use_operation_mul(self):
        self.assertEqual(use_operation('3', '*', '4'), 12)

    def test_use_operation_truediv(self):
        self.assertEqual(use_operation('16', '/', '8'), 2)

    def test_parse_math_string(self):
        self.assertEqual(parse_math_string('-4 - 4'), -8)

    def test_unbracket_1(self):
        self.assertEqual(unbracket('3 + (3+3)'), 9)

    def test_unbracket_2(self):
        self.assertEqual(unbracket('(3+3) * (3+3)'), 36)

    def test_unbracket_3(self):
        self.assertEqual(unbracket('2 + 3'), 5)


if __name__ == '__main__':
    unittest.main()