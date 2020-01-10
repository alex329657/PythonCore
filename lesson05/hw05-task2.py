"""
Task 2:
Find the Partition with Maximum Product Value
You are given a certain integer, n, n > 0. You have to search the partition or partitions, of n, with maximum product value.
Let'see the case for n = 8.
Partition                 Product
[8]                          8
[7, 1]                       7
[6, 2]                      12
[6, 1, 1]                    6
[5, 3]                      15
[5, 2, 1]                   10
[5, 1, 1, 1]                 5
[4, 4]                      16
[4, 3, 1]                   12
[4, 2, 2]                   16
[4, 2, 1, 1]                 8
[4, 1, 1, 1, 1]              4
[3, 3, 2]                   18 <---partition with maximum product value
[3, 3, 1, 1]                 9
[3, 2, 2, 1]                12
[3, 2, 1, 1, 1]              6
[3, 1, 1, 1, 1, 1]           3
[2, 2, 2, 2]                16
[2, 2, 2, 1, 1]              8
[2, 2, 1, 1, 1, 1]           4
[2, 1, 1, 1, 1, 1, 1]        2
[1, 1, 1, 1, 1, 1, 1, 1]     1

So our needed function will work in that way
findPartMaxProd(8) --> [[3, 3, 2], 18]

If there are more than one partition with maximum product value, the function should output the patitions in a length sorted way.
findPartMaxProd(10) --> [[4, 3, 3], [3, 3, 2, 2], 36]

Enjoy it!
Tests:
 describe("Example Tests", function(){
   it("Small Integers", function(){
    Test.assertSimilar(findPartMaxProd(8), [[3, 3, 2], 18]);
    Test.assertSimilar(findPartMaxProd(10), [[4, 3, 3], [3, 3, 2, 2], 36]);
   });
 });
"""
import numpy as np

dict = {1: [[1]]}

def decompose(n):
#Функция разбирает целое число на массив вариантов слагаемых


    try:
        return dict[n]
    except:
        pass
    result = [[n]]
    for i in range(1, n):
        a = n-i
        req_dict = decompose(i)
        for r in req_dict:
            if r[0] <= a:
                result.append([a] + r)
    dict[n] = result

    return result

def findPartMaxProd(n):
#Функция поиска максимального значения произведения слагаемых
    
    list_of_parts = decompose(n)
    max_prod = 0

    list_of_maxprod = []
    for i in list_of_parts:
        part_prod = np.prod(i)
        if part_prod > max_prod:
            list_of_maxprod = [i]
            max_prod = part_prod
        elif part_prod == max_prod:
            list_of_maxprod.append(i)
    list_of_maxprod.append(max_prod)

    return list_of_maxprod 

n = int(input("Введите число: "))
print(findPartMaxProd(n))





	







