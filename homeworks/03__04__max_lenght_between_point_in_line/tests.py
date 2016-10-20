# coding=utf8

import unittest
from main import parse_2_point,length_between_points, points_from_file


class SimpleTest(unittest.TestCase):

    def test_parse_2_point_int(self):
        self.assertTupleEqual(parse_2_point('123 145'), (123.0, 145.0))

    def test_parse_2_point_float(self):
        self.assertTupleEqual(parse_2_point('4.3 -11.0'), (4.3, -11.0))

    def test_length_between_points(self):
        self.assertEqual(
            length_between_points((4.3, -11.0), (123.0, 145.0)),
            196.0247178291554
        )

    def test_points_from_file(self):
        self.assertTrue(
            type(points_from_file('points.txt', parse_2_point)),
            list
        )


if __name__ == '__main__':
    unittest.main()
