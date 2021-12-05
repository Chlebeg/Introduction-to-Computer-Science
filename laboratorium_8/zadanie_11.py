#Zadanie 11
#Do funkcji przekazywana jest lista z dowolną liczbą elementów.
#Drugim argumentem funcji jest nowy alfabet.
#Ustal, czy słowa w liście są ułożone zgodnie z tym nowym alfabetem.

def list_maker():
    flag = True
    list_of_elements = []
    while flag == True:
        element = input("Write one element: ")
        list_of_elements.append(element)
        decision = input("Do you wanna add one more? [y/n] ")
        if decision != "y":
            flag = False
    return list_of_elements

def is_sorted():
    alphabet = input("Write your BRAND NEW alphabet: ")
    alphabet = alphabet[::-1]
    elements = list_maker()
    n = 0
    while n + 2 <= len(elements):
        m = 0
        while m <= len(elements[n]):
            try:
                first_letter = alphabet.index((elements[n])[m])
                second_letter = alphabet.index((elements[n+1])[m])

                if first_letter > second_letter:
                    n += 1
                    m = 10000

                elif first_letter == second_letter:
                    m += 1

                else:
                    return False

            except ValueError:
                return "something"

            except IndexError:
                if len(elements[n]) <= len(elements[n+1]):
                    n += 1
                    m = 10000
                else:
                    return False
    return True

question = "y"
while question == "y":
    a = is_sorted()
    if a == True:
        print("Your list is sorted :)")
    elif a == False:
        print("Your list isn't sorted :(")
    else:
        print("Used letters are out of alphabet >:(")
    question = input("Do you wanna try again?: [y/n] ")

#PRZYPADKI TESTOWE
# alphabet: abcdefghijklmnopqrstuvwxyz
# apple, orange, pear --> True
# abc, abd, abe, abf --> True
# def, abd, cbc, fgh --> False
# abc, abc, abc --> True
# aa, aab --> True
# aab, aa, aaa --> False

# alphabet:zyxwvutsrqponmlkjihgfedcba
# apple, orange, pear --> False
# pear, orange, apple --> True
# zyx, ghi, abc --> True