"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.

можно решить с помощью циклов и переменных, но предпочтительней с
помощью модуля collections, используя collections.Counter
"""


def common_and_longest(text: str) -> tuple:
    list_text = [text]
    common = list_text[0]
    longest = list_text[0]
    for i in range(1, len(list_text)):
        if len(list_text[i]) < common:
            common = list_text[i]
        elif len(list_text[i]) > longest:
            longest = list_text[i]
    return common, longest


if __name__ == '__main__':
    assert common_and_longest(
        "привет пока ялюблюpython привет"
    ) == ('привет', 'ялюблюpython')
    print('Решено!')
