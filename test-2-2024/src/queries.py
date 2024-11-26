from abc import ABC, abstractmethod

from model import Aircraft


class Queries(ABC):
    """
    Defines exercises.
    """

    @abstractmethod
    def get_count_of_manufacturer(self, manufacturer: Aircraft.Manufacturer) -> int:
        """
        Visszaadja azt, hogy hány típus tartozik a paraméterként megkapott gyártóhoz.

        :param manufacturer: a gyártó
        :return: a darabszám
        """

    @abstractmethod
    def order_by_year_desc_number_asc(self) -> list[Aircraft]:
        """
        Visszaadja az eredeti lista egy, a következő szempontok szerint rendezett másolatát:

        * a bemutatás éve szerint csökkenő sorrend
        * a típus azonosítója szerint növekvő sorrend

        :return: a rendezett lista
        """

    @abstractmethod
    def get_counts_by_manufacturers(self) -> dict[Aircraft.Manufacturer, int]:
        """
        Visszaad egy olyan szótárat, mely gyártónként tartalmazza a típusok számát.

        :return: a szótár
        """

    @abstractmethod
    def get_type_with_most_configurations(self) -> Aircraft:
        """
        Visszaadja azt a típust, mely a legtöbb különböző konfigurációval rendelkezik.

        Ha több ilyen típus is lenne, akkor a legelsőt adja vissza.

        :return: a típus
        """

    @abstractmethod
    def get_latest_type_by_manufacturer(self, manufacturer: Aircraft.Manufacturer) -> Aircraft:
        """
        Visszaadja a paraméterként megkapott gyártó legújabb típusát.

        Egy beszédes üzenetű `AssertionError` kivételt dob, ha a megadott gyártó nem szerepel egyetlen típusnál sem.

        :return: a típus
        """
