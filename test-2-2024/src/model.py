from __future__ import annotations
from enum import Enum
from dataclasses import field, dataclass
@dataclass
class Aircraft:
    number: str
    year: int
    manufacturer: str
    configurations: list
    def __init__(self, number:str, year:int, manufacturer: str = "AIRBUS", configurations: list = []):
        self.number = number
        self.year = year
        self.manufacturer = manufacturer
        self.configurations = configurations
    def __repr__(self):
        return f"{self.number}, {self.year}, {self.manufacturer}"
    def __eq__(self, other):
        return isinstance(self, other) and self.number == other.number
    def __hash__(self):
        return hash(self.number)
class Manufacturer(Enum):
    AIRBUS = "Airbus"
    BOEING = "Boeing"
    EMBRAER = "Embraer"
class Configuration:
    code: str
    economy: int
    buisness: int
    def __init__(self, code: str, economy: int, buisness: int):
        self.code = code
        self.economy = economy
        self.buisness = buisness
    def __eq__(self, other):
        return isinstance(self, other) and self.code == other.code
    def __hash__(self):
        return hash(self.code)