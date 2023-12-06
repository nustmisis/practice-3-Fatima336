# -*- coding: utf-8 -*-
"""
Для каждого набора входных и выходных строк требуется написать два выражения:
регулярное выражение для поиска и строку замены, при применении которых строка
ввода преобразуется в строку вывода.

Задача была взята из курса http://cs.mipt.ru/advanced_python/lessons/lab12.html

Для корректной работы автоматических тестов не переименовывайте переменные
PATTERN_1, ..., PATTERN_4, REPL_1, ... REPL_4!
"""


# Пример:


# ввод       вывод
# a b c ---> a bb c
# b b a ---> bb bb a
# a c a ---> a c a
_PATTERN_0 = r"(b)"  # строка поиска
_REPL_0 = r"\1\1"  # строка замены


# Ваше решение:


# aAc   ---> a!A!c
# aZc   ---> a!Z!c
# aZZc  ---> a!Z!!Z!c
# aBaCa ---> a!B!a!C!a
PATTERN_1 = r"([A-Z])"
REPL_1 = r'!\g<1>!'


# abc    ---> abc
# abbc   ---> abc
# azzzc  ---> azc
# arrrrc ---> arc
# xxxxxx ---> x
PATTERN_2 = r"(.)\1*"
REPL_2 = r"\1"


# this is text         ---> this is text
# this is is text      ---> this *is* text
# this is is is text   ---> this *is* text
# this is text text    ---> this is *text*
# this is is text text ---> this *is* *text*
PATTERN_3 = r"(\b\w+\b)(\s+\1)+"
REPL_3 = r"*\1*"

# one two three —-> two one three
# dog cat wolf —-> cat dog wolf
# goose car rat —-> goose rat car

PATTERN_4 = r"^(\b\w{1,4}\b)\s+(\b\w+\b)(\s+\b\w+\b)?|(\b\w{5,}\b)\s+(\b\w+\b)\s+(\b\w+\b)"
REPL_4 = lambda m: (m.group(2) + " " + m.group(1) + (m.group(3) if m.group(3) else "")) if m.group(1) else (m.group(4) + " " + m.group(6) + " " + m.group(5))