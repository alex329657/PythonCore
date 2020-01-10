def digits_recursive(n, digits=[]): 
    return digits_recursive(n // 10, [n % 10] + digits) if n else digits or [0]

i = int(input("Введите целое не отрицательное число: "))
list = digits_recursive(i)
#print(list)
result = []
for k in list:
    if k != 0:
        result += "@"*k + "~"
    else:
        result += "~~"
print ("".join(result))    
#print(result)
