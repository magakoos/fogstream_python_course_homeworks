# coding=utf8

# 2. Дана строка, состоящая из слов, разделенных пробелами. 
# Сформировать новую строку со следующими свойствами:
# a) все слова в нижнем регистре, кроме первой буквы первого слова;
# б) все ссылки в словах заменяются на "[ссылка запрещена]";
# в) все email заменяются на "[контакты запрещены]";
# г) все слова длины более 3 символов, содержащие только цифры, удаляются.
# Решить 2мя способами - встроенные функции и с помощью регулярных выражений.

import re
from string import digits

REPLASED = {
    'email': '[Контакты запрещены]',
    'url': '[Ссылка запрещена]'
}


def replace_by_str_function(string):
    url_paterns = ['http://', 'https://']
    email_pattern = '@'
    result = []
    for part in string.split(' '):
        if part.find(email_pattern) > 0:
            part = REPLASED['email']
        for patern in url_paterns:
            if part.startswith(patern):
                part = REPLASED['url'] 
        if part.isdigit() is False or len(part) <= 3:
            result.append(part)
    result = ' '.join(result)
    return result[0].upper() + result[1:]


def replace_by_re(string):
    url = re.compile(r'http[s]?\://[\w./]*')
    email = re.compile(r'[\w.]+@\w+[.]\w+')
    digit = re.compile(r'[ ]?\d\d\d\d+')

    string = re.sub(url, REPLASED['url'], string)
    string = re.sub(email, REPLASED['email'], string)
    string = re.sub(digit, '', string)

    string = re.sub(r'^\w?', string[0].upper(),  string)

    return string


def main():
    string = 'test 12 case 1234 http://www.example.com 123 https://www.example.com m.a.gomza@yandex.ru'
    print(replace_by_str_function(string))
    print(replace_by_re(string))

if __name__ == '__main__':
    main()
