"""
Task 3: Shortest Word
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
Examples
"bitcoin take over the world maybe who knows perhaps" --> 3)
"turns out random test cases are easier than writing out basic ones" --> 3)
"lets talk about javascript the best language" --> 3)
"i want to travel the world writing code one day" --> 1)
"Lets all go on holiday somewhere very cold" --> 2)
"""
print("Введите строку: ")
lst = [i for i in input().split()]
shortest = len(lst[0])
for word in lst:
    word_len = len(word) 
    if word_len < shortest:
        shortest = word_len
print("Длинна самого короткого слова:", shortest)
    


