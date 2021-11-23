flag = True
a = str("yes")
list2 = []
while a == "yes":
    while flag == True:
        try:
            fullcode = str(input("Write the message: "))
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