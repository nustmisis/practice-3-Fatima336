# -*- coding: utf-8 -*-
"""
Напишите функцию которая на вход получает строку с госномером автомибиля и
выводит к какому типу относится данный госномер, или возвращает Fail! если это
не госномер.

Типы гос.номеров:

Тип |    Пример
----+----------
 1А | с227на 69
 1Б |  ао365 78
  2 | ан7331 47
  3 | 3733мм 55

Для корректной работы автоматических тестов не переименовывайте функцию
get_plate_type!
"""

import re


def get_plate_type(plate):
    if plate == ' '.join(re.findall('[а-я]{1}\d{3}[а-я]{2}\s\d{2}', plate)):
        return "1А"
    elif plate == ' '.join(re.findall('[а-я]{2}\d{3}\s\d{2}', plate)):
        return "1Б"
    elif plate == ' '.join(re.findall('[а-я]{2}\d{4}\s\d{2}', plate)):
        return 2
    elif plate == ' '.join(re.findall('\d{4}[а-я]{2}\s\d{2}', plate)):
        return 3
    else:
        return "Fail!"

text = input()
get_plate_type(text)    
