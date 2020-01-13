"""
Task 4:
Создать массив «Список покупок». Каждый элемент массива является объектом, который содержит название продукта, необходимое количество и куплен или нет. 
Написать несколько функций для работы с таким массивом.
  1. Вывод всего списка на экран таким образом, чтобы сначала шли некупленные продукты, а потом – купленные.
  2. Добавление покупки в список. Учтите, что при добавлении покупки с уже существующим в списке продуктом, необходимо увеличивать количество в 
  существующей покупке, а не добавлять новую.
  3. Покупка продукта. Функция принимает название продукта и отмечает его как купленный.
"""
shoppinglist = {}
print("Введите через пробел название продукта и необходимое количество:")
while True:
  new_record = [s for s in input().split()]
  print(new_record)
  new_key = new_record[0]
  if shoppinglist.get(new_key) == None:
    print(shoppinglist)
    shoppinglist[new_key] = [int(new_record[1]), False]
  else:
    shoppinglist[new_key] = [shoppinglist[new_key][0] + int(new_record[1]), shoppinglist[new_key][1]] 
  print(shoppinglist)
  s = input("Continue?")
  if s == str(1):
    continue
  elif s == str(2):
    shoppinglist[new_key] = [shoppinglist[new_key][0], True]
  else:
    break
    