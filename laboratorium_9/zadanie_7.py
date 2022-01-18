#Zadanie 7.
#Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n×n wypełnioną liczbami naturalnymi.
#Dla danej tablicy należy napisać funkcję, która będzie zwracała wartość True w przypadku, gdy w każdym wierszu i każdej
#kolumnie występuje co najmniej jedno 0 oraz wartość False w przeciwnym przypadku.
#Wymiar tablicy powinien być definiowany przez użytkownika.

def grid_maker(size):
    number_grid = []
    while len(number_grid) < size:
        row = []
        for i in range(0,size):
            number = int(input("Add one number: "))
            row.append(number)
        number_grid.append(row)
        print("Your row",row)
    return number_grid

def line_checker(size,grid):
    #grid = grid_maker(size)
    #print(grid)
    value = 0
    for row in grid:        #Sprawdzamy elementy w wierszach
        flag = False
        for element_row in row:
            if element_row == 0:
                flag = True
        if flag != True:
            return False

    while value < size:     #Sprawdzamy elementy w kolumnach
        flag = False
        for row in grid:
            if row[value] == 0:
                flag = True
        if flag != True:
            return False
        value += 1
    return True

if __name__ == '__main__':
    question = "y"
    while question == "y":
        try:
            size = int(input("What size do you want? (I only accept integers :> ) "))
            a = line_checker(size)
            if a == True:
                print("True")
            elif a == False:
                print("False")
            else:
                print("Dunno something is wrong")
        except ValueError:
            print("Give me an integer!!")
        question = input("Do you wanna try again?: [y/n] ")

#Szukamy czy każdy wiersz ma 0
#Szukamy czy każda kolumna ma 0

#PRZYPADKI TESTOWE:
# size = 2, grid = [[1, 0], [0, 1]] --> True
# size = 2, grid = [[0, 1], [0, 1]] --> False

# size = 3, grid = [[0, 1, 1], [0, 1, 1], [0, 1, 1]] --> False
# size = 3, grid = [[0, 1, 1], [1, 0, 1], [1, 1, 0]] --> True
# size = 3, grid = [[0, 1, 1], [1, 1, 0], [1, 0, 1]] --> True

# size = 7, grid = [[0, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 0]] --> True