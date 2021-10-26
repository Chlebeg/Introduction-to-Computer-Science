val1 = int(input("Wpisz pierwszą liczbę:"))
val2 = int(input("Wpisz drugą liczbę:"))

if val1 < 0 and val2 < 0:
    print("Nieprawidłowa wartość, liczby <0")
    exit()

if val1 < 0:
    val1 = abs(val1)

if val2 < 0:
    val2 = abs(val2)

a = val1 + val2
b = val1 - val2
c = val1 * val2
d = val1 / val2
e = val1 ** 2
f = val2 ** 2

print(a)
print(b)
print(c)
if c == 10:
    print("Yay!")
print(d)
print(e)
print(f)


