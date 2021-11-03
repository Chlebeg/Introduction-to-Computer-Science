a = "T"
print('Ten kalkulator obsługuje: dodawanie[+], odejmowanie[-], mnożenie[*], dzielenie[/], potęgowanie[**], pierwiastkowanie[^], losowanie[x]')
print('Proszę wpisywać sam znak odpowiedni do danego działania')

while a == "T":
    operation = str(input('Co chcesz zrobić?'))

    if operation == "+":
        val1 = float(input("Wpisz pierwszą liczbę:"))
        val2 = float(input("Wpisz drugą liczbę:"))
        print("Wynik:",val1 + val2)

    elif operation == "-":
        print(2)

    elif operation == "*":
        print(3)

    elif operation == "/":
        print(4)

    elif operation == "**":
        print(5)

    elif operation == "^":
        print(6)

    else:
        print("zła operacja")

    a = str(input('Czy chcesz wykonać kolejne obliczenie?[T]/[N]'))

print("Koniec obliczeń")