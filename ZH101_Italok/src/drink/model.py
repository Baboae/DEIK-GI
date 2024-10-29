#region importok
from __future__ import annotations
from functools import total_ordering
#endregion
@total_ordering
#region Drink Osztály létrehozása - 1. feladat
class Drink():
    nev: str
    _kiszereles: str
    __ar: int
    #region konstruktor - 2. feladat
    def __init__(self, nev: str, ar: int, kiszereles: str = "5 dl"):
        self.nev = nev
        self.__ar = ar
        self.__kiszereles = kiszereles
    #endregion
    #region tulajdonságok - 3. feladat
    @property
    def kiszereles(self) -> str:
        return self.__kiszereles
    @property
    def ar(self) -> int:
        return self.__ar
    @ar.setter
    def ar(self, ar) -> None:
        self.__ar = ar
    #endregion
    #region __repr__ - 4. feladat
    def __repr__(self):
        return f"{self.nev}{self.ar}{self.kiszereles}"
    #endregion
    #region __str__ - 5. feladat
    def __str__(self):
        return f"{self.nev}, {self.kiszereles}, {self.ar} Ft"
    #endregion
    #region __eq__ - 6. feladat
    def __eq__(self, other) -> bool:
        return isinstance(other, Drink) and (self.nev, self.ar, self.kiszereles) == (other.nev, other.ar, other.kiszereles)
    #endregion
    #region __lt__ - 7. feladat
    def __lt__(self, other) -> bool:
        return isinstance(other, Drink) and (-self.ar, self.kiszereles, self.nev) < (-other.ar, other.kiszereles, other.nev)
    #endregion
    #region Statikus metódusok - 8. - 16. feladat
    #region 8. feladat
    @staticmethod
    def kiszerelesek(drinks: list[Drink], name: str) -> list:
        filtered = []
        for drink in drinks:
            if drink.nev == name and drink.kiszereles not in filtered:
                filtered.append(drink.kiszereles)
        return filtered
    #endregion
    # region 9. feladat
    @staticmethod
    def kulonbozo_kiszerelesek(drinks: list[Drink]) -> int:
        lst = []
        for drink in drinks:
            if drink.kiszereles not in lst:
                lst.append(drink.kiszereles)
        return len(lst)
    # endregion
    #region 10. feladat
    @staticmethod
    def dragabbak_szama(drinks: list[Drink], price: int) -> int:
        lst = []
        for drink in drinks:
            if drink.ar > price:
                lst.append(drink.kiszereles)
        return len(lst)
    #endregion
    # region 11. feladat
    @staticmethod
    def dragabb_kiszerelesek_szama(drinks: list[Drink], price: int) -> int:
        lst = []
        for drink in drinks:
            if drink.ar > price and drink.kiszereles not in lst:
                lst.append(drink.kiszereles)
        return len(lst)
    # endregion
    # region 12. feladat
    @staticmethod
    def italok_szama_kiszerles_szerint(drinks: list[Drink], servings:set[str]) ->int:
        counter = 0
        for drink in drinks:
            if drink.kiszereles in servings:
                counter += 1
        return counter
    # endregion
    # region 13. feladat
    @staticmethod
    def kiszerelesek_darabszam(drinks: list[Drink]) -> dict:
        kdb: dict[str, int] = {}
        for drink in drinks:
            if drink.kiszereles not in kdb:
                kdb[drink.kiszereles] = 1
            else:
                kdb[drink.kiszereles] += 1
        return kdb
    # endregion
    # region 14. feladat
    @staticmethod
    def kiszerelesek_italok(drink: list[Drink]) -> dict:
        ki: dict[str, set[str]] = {}
        for drink in drink:
            if drink.kiszereles not in ki:
                ki[drink.kiszereles] = set()
            ki[drink.kiszereles].add(drink.nev)
        return ki
    # endregion
    # region 15. feladat
    @staticmethod
    def atlagnal_dragabb_italok(drinks: list[Drink]) -> set[str]:
        dragabb: set[str] = set()
        osszes = 0
        for drink in drinks:
            osszes+=drink.ar
        atlag_ar = osszes/len(drinks)
        for drink in drinks:
            if drink.ar > atlag_ar:
                dragabb.add(drink.nev)
        return dragabb
    # endregion
    # region 16. feladat
    @staticmethod
    def atlagnal_dragabbak_listaja(drinks: list[Drink]) -> list[Drink]:
        osszes = sum(drink.ar for drink in drinks)
        atlag = osszes/len(drinks)
        # A list comprehension meg uj dolog nekem szoval handle with care, nem fix h mukodik.
        return [drink for drink in drinks if drink.ar > atlag]
    # endregion
    #endregion
#endregion
#region Szeszesitalokat ábrázoló osztály - 1. feladat
class Alcohol(Drink):
    #region Konstruktor - 2. feladat
    __alc: float
    def __init__(self, nev: str, ar: int, kiszereles: str, alc: float):
        super().__init__(nev, ar, kiszereles)
        self.__alc = alc
    #endregion
    #region Tulajdonságok - 3. feladat
    @property
    def alc(self) -> float:
        return self.__alc
    @alc.setter
    def alc(self, value: float) -> None:
        self.__alc = value
    #endregion
    #region __repr__ - 4. feladat
    def __repr__(self):
        return f"{super().__repr__()}, {self.__alc}"
    #endregion
    #region __str__ - 5. feladat
    def __str__(self):
        return f"{self.alc}% alkoholtartalmú {super().__str__()}"
    #endregion
    #region Statikus metódus - 6. feladat
    @staticmethod
    def szeszesitalok(drinks: list(Drink), name) -> list:
        filtered = [Alcohol]
        for drink in drinks:
            if isinstance(drink, Alcohol):
                filtered.append(drink)
    #endregion
#endregion