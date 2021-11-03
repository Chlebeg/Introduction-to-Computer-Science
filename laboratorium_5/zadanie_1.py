#Zadanie 1. Napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.

#Założenie:
val1 = 0
val2 = 1
val3 = val1 + val2

#Printujemy trzy pierwsze liczby(z założenia):
print(val1)
print(val2)
print(val3)

#Każda kolejna liczba jest tworzona przez pętle "while" ...
#Aż do momentu gdy pętla miałaby wyprodukować liczbę > 1 000 000:
while val2 + val3 < 1000000:
    val1 = val2
    val2 = val3
    val3 = val1 + val2
    print(val3)
