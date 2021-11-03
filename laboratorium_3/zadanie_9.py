x = 'tak'
saldo = float(100)
pin = str(input('Wybierz swój PIN:'))
print('Twoj PIN:',pin)
print('Twoje saldo wynosi:',saldo)

while x == 'tak':
    pin2 = str(input('Podaj PIN:'))

    if pin2 == pin:
        print('Właściwy PIN')
        operacja = str(input('Podaj komendę"wpłata","wypłata","sprawdź_saldo":'))

        if operacja == "wpłata":
            print('Wpłacasz pieniądze')
            a = int(input('Ile chcesz Wpłacić?'))
            saldo = saldo + a
            print('Wpłaciłeś',a)
            print('Twoje saldo wynosi', saldo)

        elif operacja == "wypłata":
            print('Wypłacasz pieniądze')
            a = int(input('Ile chcesz Wypłacić?'))

            if a > saldo:
                print('Nie masz tyle pieniędzy na koncie')
            else:
                saldo = saldo - a
                print('Wypłaciłeś',a,'     Twoje saldo wynosi:',saldo)

        elif operacja == "sprawdź_saldo":
                print('Twoje saldo wynosi:',saldo)

        else:
            print('Niewłaściwa komenda')

    else:
        print('Zły PIN')

    x = input('Czy chcesz wykonać kolejną operację?[tak/nie]:')

print('Koniec operacji')