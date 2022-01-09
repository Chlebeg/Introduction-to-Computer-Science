# Zadanie 12.
# Rozwiąż rekurencyjnie problem Wież Hanoi. Wskaż kolejne ruchy, które należy wykonać.

# WIEŻA HANOI - ZASADY:
# -dowolna liczba [n] krążków o różnych średnicach
# -trzy słupki [A,B,C] na których te krążki są położone
# -musimy przełożyć krążki z lewego słupka na prawy ALE:
#       +można przekładać tylko jeden krążek jednocześnie
#       +nie można kłaść krążka o większej średnicy na krążku o mniejszej średnicy
#       +chcemy rozwiązać przy jak najmniejszej liczbie ruchów


def solve_Hanoi_Tower(size, A, B, C): # A = skąd przesuwamy krążek, B = dokąd przesuwamy krążek
    if size == 1:
        print("Przesuń krążek", size, "z", A, "do", C)
        return
    if size != 0:
        solve_Hanoi_Tower(size-1, A, C, B)
        print("Przesuń krążek", size, "z", A, "do", C)
        solve_Hanoi_Tower(size-1, B, A, C)

solve_Hanoi_Tower(3,"A","B","C")
print(" ")
solve_Hanoi_Tower(4,"A","B","C")

def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, destination, auxiliary)
    print ("Move disk",n,"from source",source,"to destination",auxiliary)
    TowerOfHanoi(n-1, destination, auxiliary, source)
