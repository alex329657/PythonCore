from random import randrange as rnd
print("Давай сыграем в игру 'Камень-Ножницы-Бумага.'")
print("Выбери один из вариантов:\n 1. Камень.\n 2. Ножницы.\n 3. Бумага.")
usr = int(input())
ai = rnd(1, 3)
 