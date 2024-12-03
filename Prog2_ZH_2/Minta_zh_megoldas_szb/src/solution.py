from src.common.repository import Repository
from src.queries import Queries
from src.model import Aircraft
from typing import cast

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

    @property
    def entities(self) -> list[Aircraft]:
        return cast(list[Aircraft], super().entities)

    def get_count_of_manufacturer(self, manufacturer: Aircraft.Manufacturer) -> int:
        c = 0
        for i in self.entities:
            if i.manufacturer == manufacturer:
                c+=1
        return c

    def order_by_year_desc_number_asc(self) -> list[Aircraft]:
        return sorted(self.entities, key=lambda e: (-e.year, e.number))

    def get_latest_type_by_manufacturer(self, manufacturer: Aircraft.Manufacturer) -> Aircraft:
        lst = sorted(self.entities, key=lambda e: -e.year)
        r = " "
        for l in lst:
            if l.manufacturer == manufacturer:
                r = l
        if r == " ":
            raise AssertionError(f"There is not a single aircraft made by '{manufacturer}'.")
        return r
    def get_type_with_most_configurations(self) -> Aircraft:
        max_c = 0
        max_c_ac = None
        for aircraft in self.entities:
            if len(aircraft.configurations) > max_c:
                max_c = len(aircraft.configurations)
                max_c_ac = aircraft
        return max_c_ac
    def get_counts_by_manufacturers(self) -> dict[Aircraft.Manufacturer, int]:
        rtdct = {}
        for i in self.entities:
            if i.manufacturer not in rtdct:
                rtdct[i.manufacturer] = 0
            rtdct[i.manufacturer] += 1
        return rtdct
def main():
    print("\nA lista teljes tartalma:\n")
    repository = Solution(r"../data/sample.json")
    for aircraft in repository.entities:
        print(aircraft)
    print("\nRendezve évjárat és szám szerint:\n")
    sorted_ac_lst = repository.order_by_year_desc_number_asc()
    for r in sorted_ac_lst:
        print(r)
    print("\nSzótár:\n")
    szotar = repository.get_counts_by_manufacturers()
    for i in szotar:
        print(str(i) + ": " + str(szotar[i]))

    print(repository.get_count_of_manufacturer(Aircraft.Manufacturer.EMBRAER))
    print(repository.get_type_with_most_configurations())
if __name__ == '__main__':
    main()