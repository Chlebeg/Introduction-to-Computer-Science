val1 = int(input("podaj wielkość choinki:"))

print(' ' * (val1 - 1) + 'X')

for i in range(1,val1):
    print(' ' * (val1 - i - 1) + '*' * (i * 2 + 1))

print(' ' * (val1 - 1) + 'U')

