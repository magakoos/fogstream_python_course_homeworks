# coding=utf8

import unittest
from main import replace_by_str_function, replace_by_re

class SimpleTest(unittest.TestCase):

    def test_replace_by_str_function(self):
        self.assertEqual(
            replace_by_str_function(
                'test 12 case 1234 http://www.example.com 123 https://www.example.com m.a.gomza@yandex.ru'
            ),
            'Test 12 case [Ссылка запрещена] 123 [Ссылка запрещена] [Контакты запрещены]'
        )

    def test_replace_by_re(self):
        self.assertEqual(
            replace_by_re(
                'test 12 case 1234 http://www.example.com 123 https://www.example.com m.a.gomza@yandex.ru'
            ),
            'Test 12 case [Ссылка запрещена] 123 [Ссылка запрещена] [Контакты запрещены]'
        )

if __name__ == '__main__':
    unittest.main()
