from typing import cast

from src.common.repository import Repository
from src.model import Aircraft
from src.queries import Queries

class Solution(Repository, Queries):
    @staticmethod
    def type_mapper(values: dict[str, any]) -> Aircraft | Aircraft.Configuration:
        match values:
            case {"number": _}:
                aircraft = Aircraft(**values)
                aircraft.manufacturer = next(
                    Aircraft.Manufacturer[entry.name]
                    for entry in Aircraft.Manufacturer
                    if entry.value == aircraft.manufacturer
                )
                return aircraft
            case {"business": _}:
                return Aircraft.Configuration(**values)

        # def type_mapper(values: dict[str, any]) -> Főosztaly | Főosztály.Alosztály:
        #     match values:
        #         case {"főosztalyegyediazonosito(altalban number)": _}:
        #             főosztaly = Főosztály(**values)
        #             főosztály.enumosztály = next(
        #                 Főosztály.Enumosztály[entry.name]
        #                 for entry in Főosztály.Enumosztály
        #                 if entry.value == főosztály.enumosztály
        #             )
        #             return főosztály
        #         case {"alosztályutolsóadattagja": _}:
        #             return Főosztály.Alosztály(**values)

    @property
    def entities(self) -> list[Aircraft]:
        return cast(list[Aircraft], super().entities)

    def get_count_of_manufacturer(self, manufacturer: Aircraft.Manufacturer) -> int:
        return len(
            [
                aircraft
                for aircraft in self.entities
                if aircraft.manufacturer==manufacturer
            ]
        )
        # darabszam = 0
        # for aircraft in self.entities:
        #     if aircraft.manufacturer==manufacturer:
        #         darabszam+=1
        # return darabszam

    def order_by_year_desc_number_asc(self) -> list[Aircraft]:
        return sorted(self.entities, key=lambda aircraft: (-aircraft.year, aircraft.number))

    def get_latest_type_by_manufacturer(self, manufacturer: Aircraft.Manufacturer) -> Aircraft:
        assert len([aircraft for aircraft in self.entities if aircraft.manufacturer==manufacturer]) > 0
        return max((
            aircraft
            for aircraft in self.entities
            if aircraft.manufacturer==manufacturer
        ), key=lambda a: a.year, default=None)

    def get_type_with_most_configurations(self) -> Aircraft:
        return next(
            aircraft
            for aircraft in self.entities
            if len(aircraft.configurations)==max(
                [
                    len(aircraft.configurations)
                    for aircraft in self.entities
                ]
            )
        )

    def get_counts_by_manufacturers(self) -> dict[Aircraft.Manufacturer, int]:
        return {manufacturer: sum(1 for aircraft in self.entities if aircraft.manufacturer == manufacturer)
                for manufacturer in {aircraft.manufacturer for aircraft in self.entities}}

def main():
    repository = Solution(r"../data/sample.json")
    for aircraft in repository.entities:
        print(aircraft)
    szotar = repository.get_counts_by_manufacturers()
    for i in szotar:
        print(str(i) + ": " + str(szotar[i]) )

    legtobb = repository.get_type_with_most_configurations()
    print(f"Legtöbb konfig:{legtobb}")

    legujabb = repository.get_latest_type_by_manufacturer(Aircraft.Manufacturer.AIRBUS)
    print(legujabb)

    darab = repository.get_count_of_manufacturer(Aircraft.Manufacturer.AIRBUS)
    print(darab)

    rendezett = repository.order_by_year_desc_number_asc()
    for aircraft in rendezett:
        print(aircraft)

if __name__=="__main__":
    main()