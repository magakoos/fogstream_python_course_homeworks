# coding=utf8

import unittest
from main import check_bracket


class SimpleTest(unittest.TestCase):

    def test_check_bracket_Yes(self):
        self.assertEqual(check_bracket('(asdfasdf)'), 'Yes')

    def test_check_bracket_1_negative(self):
        self.assertEqual(check_bracket('fasfdas[asdfasdf{fasdfas(fasf'), -1)

    def test_check_bracket(self):
        self.assertEqual(check_bracket('(asdfa{sdfsa[asf{asd}fasd]fsafas'), 2)


if __name__ == '__main__':
    unittest.main()