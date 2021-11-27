#Proszę napisać program wczytujący z klawiatury dowolną ilość znaków. Program powinien wybrać tylko te znaki,
#które znajdują się pomiędzy zerami. Następnie należy wczytane znaki zamienić na kod dziesiętny ASCII wykorzystując
#funkcję ord().Należy sprawdzić i wypisać kody a następnie podać znak, który ma 5 co do wartości kod dziesiętny ASCII.
#Można założyć, że dane są poprawne i w ciągu znajduje się wystarczająca liczba elementów.
flag = True
a = str("yes")
list2 = []

while a == "yes":
    while flag == True:
        try:
            fullcode = input("Write the message: ")
            substring_start = fullcode.index("0")
            halfcode = fullcode[(substring_start + 1):]
            substring_end = halfcode.index("0")
            substring = halfcode[:(substring_end)]
            flag = False
        except ValueError:
            print("No matches found :(")

    for i in list(substring):
        value = ord(i)
        print(i,value)
        list2.append(value)

    list2.sort()
    list2.reverse()
    print(list2)

    b = list2[4]
    result = chr(b)
    print("Your result: ",result)
    a = str(input("Wanna try again?:[yes/no] "))
    flag = True