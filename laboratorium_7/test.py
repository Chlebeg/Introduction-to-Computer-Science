#Proszę napisać program wczytujący z klawiatury dowolną ilość znaków. Program powinien wybrać tylko te znaki,
#które znajdują się pomiędzy zerami. Następnie należy wczytane znaki zamienić na kod dziesiętny ASCII wykorzystując
#funkcję ord(). Należy sprawdzić i wypisać kody a następnie podać znak, który ma 5 co do wartości kod dziesiętny ASCII.
#Można założyć, że dane są poprawne i w ciągu znajduje się wystarczająca liczba elementów.
flag = True
a = str("yes")
list_substring = []
list_value = []
check = True

while a == "yes":
    while flag == True:
        try:
            fullcode = input("Write the message: ")
            while fullcode != None:
                print(fullcode)
                substring_start = fullcode.index("0")
                print(substring_start)
                halfcode = fullcode[(substring_start + 1):]
                print(halfcode)
                substring_end = halfcode.index("0")
                print(substring_end)
                substring = halfcode[:(substring_end)]
                print(substring)
                list_substring.append(substring)
                fullcode = fullcode[(substring_end + 1):]
                print(list_substring)

        except ValueError:
            flag = False


    for i in list_substring:
        value = ord(i)
        print(i,value)
        list_value.append(value)

    list_value.sort()
    list_value.reverse()
    print(list_value)

    b = list_value[4]
    result = chr(b)
    print("Your result: ",result)
    a = str(input("Wanna try again?:[yes/no] "))
    flag = True