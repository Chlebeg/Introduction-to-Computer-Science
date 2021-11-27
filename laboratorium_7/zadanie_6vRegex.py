import re
flag = True
a = str("yes")
list2 = []
while a == "yes":
    while flag == True:
        s = input("Write the message: ")
        try:
            substring = re.search('0(.+?)0', s).group(1)
            flag = False
        except AttributeError:
            print("No matches found :(")

    for i in list(substring):
        value = ord(i)
        #print(i,value)
        list2.append(value)

    list2.sort()
    list2.reverse()
    #print(list2)
    b = list2[4]
    result = chr(b)
    print("Your result: ",result)
    a = str(input("Wanna try again?:[yes/no] "))
