"""
Task 1: Василий давно занимается математическими аномалиями.
Сейчас ему открылся новый способ анализа чисел - берется
натуральное число и считается сумма всех его чисел на
которое это число делится без остатка(т.е. делителей).
Василий хочет автоматизировать эту процедуру.
Напишите функцию, которая облегчит его изыскания.

Пример работы:
Вводит 6 - Выводит 12
Вводит 10 - Выводит 18
"""

import time
def factors(n):
    results = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            results.add(i)
            results.add(int(n/i))
    return results


def factors_v2(n):
    return set(x for tup in ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0) for x in tup)

n = int(input("Введите натуральное число: "))
begin_time = time.time()
print("Сумма делителей:", sum(factors(n)))
print(time.time() - begin_time)
begin_time = time.time()
print("Сумма делителей:", sum(factors_v2(n)))
print(time.time() - begin_time)

"""
Разбор:
list = [[i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0]
sett = set(x for tup in list for x in tup)
print(list)
print(sett)
"""

