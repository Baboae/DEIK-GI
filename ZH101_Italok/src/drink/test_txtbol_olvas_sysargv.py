import sys
from drink.model import *
def main() -> None:
    while True:
        list_drinks = []
        try:
            if len(sys.argv) == 1:
                raise FileNotFoundError
            reader = open(sys.argv[1], 'r', encoding='utf-8')
            if reader == FileNotFoundError:
                raise Exception
            for r in reader:
                r = r.strip().split(';')
                if len(r) == 3:
                    list_drinks.append(Drink(r[0], int(r[2]), r[1]))
                if len(r) == 4:
                    list_drinks.append(Alcohol(r[0], int(r[2]), r[1], float(r[3])))
            reader.close()
            list_drinks.sort(key = lambda x: (-x.ar, x.kiszereles, x.nev))
            for l in list_drinks:
                print(l)
            break
        except FileNotFoundError:
            print("Hibás, vagy üres a parancssori argumentum!")
            break
if __name__ == '__main__':
    main()