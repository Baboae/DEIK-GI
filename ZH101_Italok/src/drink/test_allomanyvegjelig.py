from drink.model import *
def main()->None:
    list_drinks = []
    while True:
        try:
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
        except EOFError:
            break
if __name__ == '__main__':
    main()