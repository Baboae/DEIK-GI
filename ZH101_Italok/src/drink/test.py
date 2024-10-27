import sys
from math import trunc

from drink.model import Alcohol
from model import Drink
def main() -> None:
    list_drinks = []

    if len(sys.argv) == 1:
        raise NameError("Nincs parancssori argumentum!")
    if int(sys.argv[1]) < 1:
        raise NameError("Hibás parancssori argumentum!")
    n = int(sys.argv[1])

    for i in range(n):
        line = input()
        d = line.strip().split(";")
        name = d[0]
        serving = d[1]
        price = int(d[2])
        if len(d) == 3:
            list_drinks.append(Drink(name, price, serving))
        if len(d) == 4:
            alc = float(d[3])
            list_drinks.append(Alcohol(name, price, serving, alc))
    list_drinks.sort(key=lambda x: (-x.ar, x.kiszereles, x.nev))
    for d in list_drinks:
        print(d)
if __name__ == '__main__':
    main()