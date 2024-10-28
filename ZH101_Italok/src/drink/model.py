from __future__ import annotations
from functools import total_ordering

@total_ordering
class Drink():
    nev: str
    _kiszereles: str #vedett
    __ar: int #privat

    def __init__(self, nev: str, ar: int, kiszereles: str = "5 dl"):
        self.nev = nev
        self.__ar = ar
        self.__kiszereles = kiszereles
    @property
    def kiszereles(self) -> str:
        return self.__kiszereles
    @property
    def ar(self) -> int:
        return self.__ar
    @ar.setter
    def ar(self, ar) -> None:
        self.__ar = ar

    def __repr__(self):
        return f"{self.nev}{self.ar}{self.kiszereles}"
    def __str__(self):
        return f"{self.nev}, {self.kiszereles}, {self.ar} Ft"
    def __eq__(self, other) -> bool:
        return isinstance(other, Drink) and (self.nev, self.ar, self.kiszereles) == (other.nev, other.ar, other.kiszereles)
    def __lt__(self, other) -> bool:
        return isinstance(other, Drink) and (-self.ar, self.kiszereles, self.nev) < (-other.ar, other.kiszereles, other.nev)
    @staticmethod
    def kiszerelesek(drinks: list(Drink), name) -> list:
        filtered = []
        for drink in drinks:
            if drink.nev == name and drink.kiszereles not in filtered:
                filtered.append(drink.kiszereles)
        return filtered
class Alcohol(Drink):
    __alc: float
    def __init__(self, nev: str, ar: int, kiszereles: str, alc: float):
        super().__init__(nev, ar, kiszereles)
        self.__alc = alc

    @property
    def alc(self) -> float:
        return self.__alc
    @alc.setter
    def alc(self, value: float) -> None:
        self.__alc = value
    def __repr__(self):
        return f"{super().__repr__()}, {self.__alc}"
    def __str__(self):
        return f"{self.alc}% alkoholtartalmú {super().__str__()}"
    @staticmethod
    def szeszesitalok(drinks: list(Drink), name) -> list:
        filtered = [Alcohol]
        for drink in drinks:
            if isinstance(drink, Alcohol):
                filtered.append(drink)