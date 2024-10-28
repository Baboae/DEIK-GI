import sys
from drink.model import *
def main() -> None:
    list_drinks = []
    if len(sys.argv) == 1:
        raise NameError("Nincs parancssori argumentum!")
    if int(sys.argv[1]) < 1:
        raise NameError("Hibás parancssori argumentum!")
    n = int(sys.argv[1])
    while True:
        try:
            line = input()
            l = line.strip().split(';')
            if int(l[2]) < n:
                if len(l) == 3:
                    list_drinks.append(Drink(l[0], int(l[2]), l[1]))
                if len(l) == 4:
                    list_drinks.append(Alcohol(l[0],int(l[2]), l[1], float(l[3])))
            list_drinks.sort(key = lambda x: (-x.ar, x.kiszereles, x.nev))
            for drink in list_drinks:
                print(f"\n{drink}")
            else:
                raise NameError
        except NameError:
            print(f"Az ital drágább {n} ft-nál.")
            break
if __name__ == '__main__':
    main()
