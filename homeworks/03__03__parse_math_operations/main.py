# conding=utf8

TEST_STRING1 = '2 + 3, -4 - 4, 5 *4, 6/3'
TEST_STRING2 = '3 - 4'
TEST_STRING3 = '3 + (3+3), (3+3) * (3+3),(2+2)+1'


import re


MATH_EXPRESSION = re.compile(r'[ ]?([\d.\-]*)[ ]*([\+\*\-/])[ ]*([\d.\-]*)')
MATH_SPLITE = re.compile(r'[\+\*\-/]')


class WrongOperator(Exception):
    def __init__(self, *args, **kwargs):
        super(WrongOperator, self).__init__(*args, **kwargs)
        print('Wrong operator in expression.')


def split_explessions(comma_sep_str):
    return comma_sep_str.split(',')


def use_operation(left, operator, right):
    """
    Make arithmetic operations
    :param left: operathor
    :param operator: + | - | * | /
    :param right: operathor
    :return:
    """
    left = float(left)
    right = float(right)
    if operator == '+':
        return left.__add__(right)
    elif operator == '-':
        return left.__sub__(right)
    elif operator == '*':
        return left.__mul__(right)
    elif operator == '/':
        return left.__truediv__(right)
    else:
        raise WrongOperator


def unbracket(string):
    """
    Make free form brackets and resolve math_string.
    :param string: Math string (str)
    :return: resolved string
    """
    if type(string) == str and '(' in string:
        start = string.find('(')
        finish = string.find(')', start)
        string_in_brackets = string[start + 1:finish]
        exp = unbracket(string_in_brackets)
        string = string[:start] + str(exp) + string[finish+1:]
        return unbracket(string)
    elif type(string) != str:
        return string
    else:
        return parse_math_string(string)


def parse_math_string(math_string):
    """
    parse math string to operator and operands
    :param math_string:
    :return: resolve math operator
    """
    l_operand, operator, r_operand = re.match(
        MATH_EXPRESSION,
        math_string
    ).groups()
    return use_operation(l_operand, operator, r_operand)


def main():
    for i in split_explessions(TEST_STRING3):
        print(unbracket(i))


if __name__ == '__main__':
    main()
