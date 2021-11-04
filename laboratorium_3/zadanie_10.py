import random

a = "T"
print('Ten kalkulator obsługuje: dodawanie[+], odejmowanie[-], mnożenie[*], dzielenie[/], potęgowanie[**], pierwiastkowanie[^], losowanie[x]')
print('Proszę wpisywać sam znak odpowiedni do danego działania')

def dzialanie():
    n = str(input('Podaj liczbę lub wylosuj [x]: '))
    if n == 'x':
        while n == 'x':
            starting_point = float(input('Podaj początek zakresu: '))
            ending_point = float(input('Podaj koniec zakresu: '))
            if not starting_point > ending_point:
                n = random.uniform(starting_point,ending_point)
                print('Wylosowało: ',n)
                return float(n)
            else:
                print('Zły zakres')
    else:
        return float(n)

val1 = dzialanie()

while a == "T":
    operation = str(input('Co chcesz zrobić? '))
    val2 = dzialanie()

    if operation == "+":    val1 = val1 + val2

    elif operation == "-":  val1 = val1 - val2

    elif operation == "*":  val1 = val1 * val2

    elif operation == "/":
        if val2 == 0:
            print('Pamiętaj cholero')
        else:
            val1 = val1 / val2

    elif operation == "**": val1 = val1 ** val2

    elif operation == "^":  val1 = val1 ** (1/val2)

    else:
        print("zła operacja")

    print('Wynik ', val1)
    a = str(input('Czy chcesz wykonać kolejne obliczenie?[T]/[N] '))

print("Koniec obliczeń")
