"""
Task 1: Ремонт
Ваш любимый дядя – директор фирмы, которая делает евроремонты в офисах.
В связи с финансово-экономическим кризисом, дядюшка решил оптимизировать свое предприятие.
Давно ходят слухи, что бригадир в дядюшкиной фирме покупает лишнее количество стройматериалов,
а остатки использует для отделки своей новой дачи. Ваш дядя заинтересовался,
сколько в действительности банок краски необходимо для покраски стен в офисе длиной L метров,
шириной – W и высотой – H, если одной банки хватает на 16м2,
а размерами дверей и окон можно пренебречь? Заказов много, поэтому дядя попросил написать
программу, которая будет все это считать.

Входные данные
Пользователь вводит с клавиатуры три натуральных числа L, W, H – длину, ширину и высоту офиса в
метрах соответственно, каждое из которых не превышает 1000.

Выходные данные
Вывести на экран одно целое число – минимальное количество банок краски, необходимых для
покраски стен в офисе.
"""

L = int(input("Введите значение L: "))
if L not in range(1, 1001):
    print("Значение должно быть натуральным числом не больше 1000")
    exit()
W = int(input("Введите значение W: "))
if W not in range(1, 1001):
    print("Значение должно быть натуральным числом не больше 1000")
    exit()
H = int(input("Введите значение H: "))
if H not in range(1, 1001):
    print("Значение должно быть натуральным числом не больше 1000")
    exit()
S = (2 * L * H) + (2 * W * H)
number_of_cans = S /16
print(f"Для покраски необходимо {number_of_cans} банок краски")

