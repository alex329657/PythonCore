"""
Task 2:
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development
and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA
string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA
at all (again, except for Haskell).

More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"
"""
dna_strand = input("Введите строку первой ДНК нити: ").upper()
dna_strand2 = ""
for s in dna_strand:
    if s == "A":
        dna_strand2 += "T"
    elif s == "T":
        dna_strand2 += "A"
    elif s == "C":
        dna_strand2 += "G"
    elif s == "G":
        dna_strand2 += "C"
    else:
        print(f"Символ {s} не используется в строках ДНК нитей, пропускаем")
print("Строка второй ДНК нити:", dna_strand2) 

