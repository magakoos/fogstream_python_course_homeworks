# coding=utf8

import sys
from urllib import request
from lxml import etree


URL_CBR = 'http://www.cbr.ru/scripts/XML_daily.asp'


def request_cbr_by_code(valute_CharCode):
    response = request.urlopen(URL_CBR)
    text = response.read()
    tree = etree.fromstring(text)
    xpath_string = "//Valute[CharCode='{CharCode}']".format(
        CharCode=valute_CharCode
    )
    tree = tree.xpath(xpath_string)
    if len(tree) == 1:
        value = tree[0].xpath("./Value/text()")
        nominal = tree[0].xpath("./Nominal/text()")
        name = tree[0].xpath("./Name/text()")
        return (value[0], nominal[0], name[0])
    return False

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print('Вы выбрали валюту {code}'.format(
            code=sys.argv[1]
        ))
        valute = request_cbr_by_code(sys.argv[1])
        if type(valute) == tuple:
            output = 'Курс {name} на сегодня: {value} за {nominal}'.format(
                value=valute[0],
                nominal=valute[1],
                name=valute[2]
            )
        else:
            output = 'Ввведите другой код валюты'
        print(output)
    else:
        print('Введите символьный код валюты')
