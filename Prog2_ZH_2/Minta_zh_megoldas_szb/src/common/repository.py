from __future__ import annotations

import json
from abc import abstractmethod
from copy import deepcopy


class Repository:
    """
    Reads and stores data of a type.
    """

    _entities: list[object]

    def __init__(self, path: str) -> None:
        """
        Creates an instance.

        :param path: the path of the JSON document storing the instances of the type
        """
        with open(path, encoding="utf-8") as file:
            self._entities = json.load(file, object_hook=self.type_mapper)

    @staticmethod
    @abstractmethod
    def type_mapper(values: dict[str, any]) -> object:
        """
        Maps thw nodes of the JSON document to types.

        :param values: a dictionary representing the actual node
        :return: the corresponding object
        """

    @property
    def entities(self) -> list[object]:
        """
        Returns a view of the data

        :return: the data
        """
        return [deepcopy(d) for d in self._entities]
