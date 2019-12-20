print("Выберите вариант расчета(1-3):")
print("1. Расчет необходимого количества строк кода.")
print("2. Расчет количества возможных опозданий.")
print("3. Расчет суммы дохода.")
choice = int(input())
if choice == 1:
    print("Выбран вариант", choice)
    income = int(input("Введите сумму дохода: "))
    delays = int(input("Введите количество опозданий: "))
    number_of_lines = round((income + delays * 20) / 50 * 100, 0)
    print("Number of lines: ", str(number_of_lines))
elif choice == 2:
    print("Выбран вариант", choice)
    number_of_lines = int(input("Введите число строк кода: "))
    income = int(input("Введите сумму дохода: "))
    delays = (income - number_of_lines * 0.5) / 20
elif choice == 3:
    print("Выбран вариант", choice)
    number_of_lines = int(input("Введите число строк кода: "))
    delays = int(input("Введите количество опозданий: "))
    income = number_of_lines * 0,5 - delays * 20
else:
    print("Вариант не выбран. Выход из программы.")
    
    

