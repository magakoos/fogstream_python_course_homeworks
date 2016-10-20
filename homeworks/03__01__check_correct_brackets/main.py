# coding=utf8

checked_list = [
    '(asdfasdf)',
    '[asdfa(sf]',
    '{asfdsagsaf}',
    '(asdfasdf(fafa)]',
    '(safdasfd[fasdf]fasfd)',
    '(asdfa{sdfsa[asf{asd}fasd]fsafas)',
    '(asdf{}asdf)',
    '{asfas)fasdas}',
    'fasfdas[asdfasdf{fasdfas(fasf'
]

brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

def check_bracket(string):
    """
    Checking full set for brackets.
    return:
        'Yes' in case all brackets correct.
        int - number wrong bracket
        -1 if all bracket is open.
    """
    bracket_list = []
    for item in string:
        if item in brackets.keys():
            bracket_list.append(item)
        try:
            try:
                if item == brackets[bracket_list[-1]]:
                    bracket_list.pop()
            except IndexError:
                return -1
        except KeyError:
            return len(bracket_list)
    if len(bracket_list) > 0:
        return len(bracket_list)
    return 'Yes'


def main(lst):
    """
    Open each item in list and check bracket's full
    """
    for item in lst:
        print(check_bracket(item))


if __name__ == '__main__':
    main(checked_list)
