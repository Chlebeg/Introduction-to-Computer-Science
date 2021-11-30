#Proszę napisać program wczytujący z klawiatury dowolną ilość znaków. Program powinien wybrać tylko te znaki,
#które znajdują się pomiędzy zerami. Następnie należy wczytane znaki zamienić na kod dziesiętny ASCII wykorzystując
#funkcję ord(). Należy sprawdzić i wypisać kody a następnie podać znak, który ma 5 co do wartości kod dziesiętny ASCII.
#Można założyć, że dane są poprawne i w ciągu znajduje się wystarczająca liczba elementów.
flag = True
a = str("yes")
check = True

while a == "yes":
    list_substring = []
    final_list_sub = []
    list_value = []
    while flag == True:
        try:
            fullcode = input("Write the message: ")
            while fullcode != None:
                #print(fullcode)
                substring_start = fullcode.index("0")
                #print(substring_start)
                halfcode = fullcode[(substring_start + 1):]
                #print(halfcode)
                substring_end = halfcode.index("0")
                #print(substring_end)
                substring = halfcode[:(substring_end)]
                #print(substring)
                list_substring.append(substring)
                fullcode = fullcode[(substring_end + 1):]
                print(list_substring)

        except ValueError:
            flag = False

    if list_substring == []:
        print("No matches found :(")

    else:
        for i in list_substring:
            final_list_sub += i
            print(final_list_sub)

        if len(final_list_sub) >= 5:
            for i in final_list_sub:
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
        else:
            print("Code too short >:(")
    flag = True

#Przypadki testowe:
# Dobra dana:       s0bcdefgh0es --> reasult = d
# Wiele zer:        0ab0bc0cd0fgh0ij --> reasult = c
# Brak zer:         abcdefg --> No matches found :(
# Tylko jedno zero:             abc0ddd --> No matches found :(
# Tekst pomiędzy zerami < 5:    abd0dc0fghi --> Code too short >:(