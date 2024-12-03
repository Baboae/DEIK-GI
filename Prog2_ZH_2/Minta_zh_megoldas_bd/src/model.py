from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum

@dataclass
class Aircraft:
    number:str = field(hash=True)
    year:int = field(compare=False)
    manufacturer: Manufacturer = field(compare=False, default_factory=lambda: Aircraft.Manufacturer.AIRBUS)
    configurations: list[Configuration] = field(compare=False, repr=False, default_factory=lambda: [])

    class Manufacturer(Enum):
        AIRBUS="Airbus"
        BOEING="Boeing"
        EMBRAER="Embraer"

    @dataclass
    class Configuration:
        code:str = field(hash=True)
        economy:int = field(compare=False)
        business:int = field(compare=False)