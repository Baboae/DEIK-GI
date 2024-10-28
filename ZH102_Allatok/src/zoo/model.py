from __future__ import annotations
from functools import total_ordering


@total_ordering
class Animal():

    faj: str
    __kor: float
    _suly: float

    def __init__(self, faj: str,suly: float, kor: float=0.0):
        self.faj = faj
        self._suly = suly
        self.__kor = kor
    def __repr__(self) -> str:
        return f"{self.faj}, {self.__kor}, {self._suly}"
    def __str__(self) -> str:
        return f"{self.faj}: {self.__kor} év, {self._suly} kg"
    def __eq__(self, other) -> bool:
        return isinstance(other, Animal) and \
            (self.faj, self._suly, self.__kor) == (other.faj, other._suly, other.__kor)
    def __lt__(self, other) -> bool:
        return isinstance(other, Animal) and \
            (self.faj, -self.__kor, self._suly) < (other.faj, -other.__kor, other._suly)
    @property
    def suly(self) -> float:
        return self._suly
    @property
    def kor(self) -> float:
        return self.__kor
    @kor.setter
    def kor(self, kor: float):
        self.__kor = kor
    @staticmethod
    def eletkorok(allatok: list[Animal], fajnev: str) -> list:
        retlist = []
        for allat in allatok:
            if allat.faj == fajnev and allat.kor not in retlist:
                retlist.append(allat.kor)
        return retlist
class Mammal(Animal):
    __labak: int
    def __init__(self, labak: int, faj: str, suly: float, kor: float = 0.0,):
        super().__init__(faj, suly, kor)
        self.__labak = labak
    @property
    def labak(self) -> int:
        return self.__labak
    @labak.setter
    def labak(self, value) -> None:
        self.__labak = value
    def __repr__(self):
        return f"{super().__repr__()}, {self.__labak}"
    def __str__(self):
        return f"{super().__str__()} (lábak száma: {self.__labak})"
