a = int(input("Введите значение a: "))
if a not in range(1, 101):
	print("Значение а должно быть в диапазоне [1:100].")
	exit()
b = int(input("Введите значение b: "))
if b not in range(1, 101):
	print("Значение b должно быть в диапазоне [1:100].")
	exit()
n = int(input("Введите значение n: "))
if n not in range(1, 101):
	print("Значение n должно быть в диапазоне [1:100].")
	exit()
weight = a * b * n * 2
print(weight)