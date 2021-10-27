val1 = int(input("Wpisz pierwszą liczbę:"))
val2 = int(input("Wpisz drugą liczbę:"))

'''Zakładamy że urzytkownik podaje przedział czyli val1 > val2'''

zakres = val2 - val1 + 1

for number in range(val1,val2+1):
    if zakres > 20:
        a = float((val1 + val2)/2)
        d = int((val1 + val2)/2)
        b = int(a-3)
        c = int(a+3)
        if a > d:
            b = b+1
            for i in range(b,d):
                print(i)
            for i in range(d,c+1):
                print(i)
        else:
            for i in range(b,d):
                print(i)
            for i in range(d+1,c+1):
                print(i)
        exit()
    print(number)
