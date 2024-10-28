import sys

from zoo.model import Animal
from zoo.model import Mammal
def main():
    if len(sys.argv) == 1:
        raise NameError("Nincs elég parancssori argumentum!")
    if int(sys.argv[1]) < 1:
        raise ValueError("Hibás a parancssori argumentum!")
    n = int(sys.argv[1])
    allatok = []
    for i in range(n):
        animals = input()
        a = animals.strip().split(";")
        faj = a[0]
        kor = float(a[1])
        suly = float(a[2])
        if len(a) == 3:
            allatok.append(Animal(faj, suly, kor))
        if len(a) == 4:
            labak = int(a[3])
            allatok.append(Mammal(labak, faj, suly, kor))
    allatok.sort(key = lambda a: (a.faj)) ## itt meg az output szerint kor szerint \
    # csokkeno sorrendbe kene rendezni, csak az privat, es nemtudom h kene xddf
    for a in allatok:
        print(a)
if __name__ == '__main__':
    main()