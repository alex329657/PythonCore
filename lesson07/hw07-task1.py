"""
Given a closed interval [n, m], return the even number that is the strongest in the interval. If multiple solutions
exist return the smallest strongest even number
"""
def count(num, counter=0):
    if num % 2 == 0:
        return count(num/2, counter + 1)
    else:
        return counter
even_number = 0
strongest = 0
list = [int(i) for i in input('Введите данные: ').lower().strip('[]').split(', ')]
for n in range(list[0], list[1]+1):
    if n % 2 == 0:
        strong_counter = count(n)
        if strong_counter > strongest:
            strongest = strong_counter
            even_number = n
        elif strong_counter == strongest:
            even_number = min(even_number, n)
print(even_number)



