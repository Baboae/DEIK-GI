from functools import total_ordering
from __future__ import annotations

@total_ordering
class Animal():
    pass
    def __init__(self, name, age):
        pass
    def __repr__(self):
        pass
    def __str__(self):
        pass
    def __eq__(self, other):
        pass
    def __lt__(self, other):
        pass
    @staticmethod
    def metodus(self):
        pass
class Mammals(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        @property
        def tulajdonsag(self):
            pass
        @tulajdonsag.setter
        def tulajdonsag(self, value):
            pass
        def __repr__(self):
            super().__repr__()
        def __str__(self):
            super().__str__()
