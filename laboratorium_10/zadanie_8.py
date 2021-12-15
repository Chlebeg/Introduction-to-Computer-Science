# Zadanie 8.
# Wykorzystując funkcje, proszę napisać program, który umożliwia dodawanie, odejmowanie i mnożenie dwóch plików.
# Pliki A i B zawierają po 7 słów w kolejnych linijkach, co ważne bez powtórzeń w obrębie pliku,
# między plikami możliwe jest powtarzanie.
# [+] Dodawanie to operacja, w wyniku której tworzony jest plik C zawierający maksymalnie 7 słów w kolejnych linijkach.
# C zawiera wszystkie słowa z A i B bez powtórzeń tak, że naprzemiennie w kolejnych linijkach ułożone są słowa
# występujące tylko w A i B (jeśli występują powtórki umieszczone są na końcu pliku).
# [-] Odejmowanie z kolei to słowa występujące tylko w A a nie w B umieszczone bez powtórzeń po 7 w linijce.
# [*] W wyniku mnożenia tworzony jest plik C, który ma 7 razy wpisane powtarzające się słowo w osobnej linii.
# Słowa są w takim wypadku ułożone alfabetycznie. Należy obsłużyć wyjątki.

def list_maker(file_name):
    file = open(file_name + ".txt","r")
    workable_file = file.read()
    list = []
    while workable_file != "":
        try:
            element_end = workable_file.index(" ")
        except ValueError:
            element_end = len(workable_file)
        try:
            element_newline = workable_file.index("\n")
        except ValueError:
            element_newline = 100000

        if element_newline < element_end:
            element = workable_file[:element_newline]
            workable_file = workable_file[element_newline + 1:]
        else:
            element = workable_file[:element_end]
            workable_file = workable_file[element_end + 1:]
        list.append(element)
    file.close()
    return list

question = "y"
while question == "y":
    action = input("What action you want to do: addition [+], subtraction [-], multiplication [*]? ")

    first_file_name = "file_A"
    second_file_name = "file_B"
#    first_file_name = input("Write name of first file(without .txt): ")
#    second_file_name = input("Write name of second file(without .txt): ")

    list_A = list_maker(first_file_name)
    list_B = list_maker(second_file_name)
    result_file = open("file_C.txt", "w")

    if action == "+":
        odd_lines = []
        even_lines = []
        reruns_list = []

        for element_A in list_A:
            flag = False
            for element_B in list_B:
                if element_A == element_B:
                    flag = True
            if flag == True:
                odd_lines.append(element_A)
                reruns_list.append(element_A)
            else:
                odd_lines.append(element_A)

        for element_B in list_B:
            flag = False
            for element_A in list_A:
                if element_B == element_A:
                    flag = True
            if flag == False:
                even_lines.append(element_B)

        final_list = []
        n = 0
        while len(odd_lines) + len(even_lines) > len(final_list):
            final_list.extend(odd_lines[n:n+7])
            final_list.extend(even_lines[n:n+7])
            n += 7
        final_list.extend(reruns_list)

        m = 0
        for element in final_list:
            result_file.write(element + " ")
            m += 1
            if m % 7 == 0:
                result_file.write("\n")

    elif action == "-":
        m = 0
        for element_A in list_A:
            flag = False
            for element_B in list_B:
                if element_A == element_B:
                    flag = True
            if flag != True:
                result_file.write(element_A+" ")
                m += 1
                if m % 7 == 0:
                    result_file.write("\n")

    elif action == "*":
        m = 0
        reruns_list = []
        for element_A in list_A:
            flag = False
            for element_B in list_B:
                if element_A == element_B:
                    flag = True
            if flag:
                reruns_list.append(element_A)

        reruns_list.sort()

        for element in reruns_list:
            for i in range(7):
                result_file.write(element+" ")
            result_file.write("\n")

    else:
        print("There is no operation like this: ",action)

    result_file.close()
    question = input("Do you wanna try again? [y]/[n] ")