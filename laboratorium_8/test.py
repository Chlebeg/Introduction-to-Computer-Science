def is_it_pierwsza(num):

    if num == 2 or num == 3:
        return True

    if num % 2 == 0 or num % 3 == 0 or num < 2:
        return False

    k = 5
    while k < num**.5:

        if num % k == 0:
            return False
        k+=2

        if num % k == 0:
            return False
        k+=4

    return True

a = is_it_pierwsza(361)
print(a)