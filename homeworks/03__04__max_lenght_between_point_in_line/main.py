# coding=utf8
import re
import math

FILENAME = 'points.txt'


def parse_2_point(file_line):
    """
    :param file_line: string with two numbers separated by space.
    :return: tuple with 2 points in float
    """
    left, rigth = re.match(r'([\-\d.]+)[ ]+([\-\d.]+)', file_line).groups()
    pair = (float(left), float(rigth))
    return pair


def points_from_file(file, rule):
    """
    return points from file:
    :param file: filename with point
    :param rule: parsing rule
    :return: list of point pair
    """
    f = open(file, 'r')
    result = []
    for row in f.readlines():
        pair = rule(row)
        result.append(pair)
    return result


def length_between_points(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)


def key_len(item):
    return length_between_points(item[0], item[1])


def get_pair_list(file):
    point_list = points_from_file(file, parse_2_point)
    result = set()
    for i in point_list:
        for j in point_list:
            if i != j:
                result.add((i, j))
    return list(result)


def get_max_len(pair_list):
    x, y = max(pair_list, key=key_len)
    return length_between_points(x, y)


def get_min_len(pair_list):
    x, y = min(pair_list, key=key_len)
    return length_between_points(x, y)


def main():
    pair_list = get_pair_list(FILENAME)
    print('Максимальная длина между точками: {n}'.format(
        n=get_max_len(pair_list))
    )
    print('Минимальная длина между точками: {n}'.format(
        n=get_min_len(pair_list))
    )
    print(length_between_points((4.3, -11.0), (123.0, 145.0)))

if __name__ == '__main__':
    main()
