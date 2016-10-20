# coding=utf8

import unittest
from main import request_cbr_by_code


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.eur = request_cbr_by_code('EUR')

    def test_request_cbr_by_code_false(self):
        self.assertFalse(request_cbr_by_code('asdf'))

    def test_request_cbr_by_code_EUR(self):
        self.assertEqual(self.eur[2], 'Евро')


if __name__ == '__main__':
    unittest.main()
