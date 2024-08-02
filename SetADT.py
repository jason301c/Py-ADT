from abc import abstractmethod, ABC
from typing import TypeVar, Generic
from collections.abc import Iterable

__author__ = "Jason Alexander S."

"""
This file provides the template for a Set Abstract Data Type.
Operations taken from https://en.wikipedia.org/wiki/Set_(abstract_data_type)
"""


class SetADT(ABC):
    @abstractmethod
    def __init__(self, lst: Iterable[Generic] = None) -> None:
        """
        Set constructor
        :param lst: A iterable to initialize the set with
        """
        pass

    @abstractmethod
    def union(self, other: 'SetADT') -> 'SetADT':
        """
        Union operation
        :return: The union of two sets
        """
        pass

    @abstractmethod
    def intersection(self, other: 'SetADT') -> 'SetADT':
        """
        Intersection operation
        :return: The intersection of two sets
        """
        pass

    @abstractmethod
    def difference(self, other: 'SetADT') -> 'SetADT':
        """
        Difference operation
        :return: The difference of two sets
        """
        pass

    @abstractmethod
    def subset(self, other: 'SetADT') -> bool:
        """
        Subset operation
        :return: Boolean, whether self is a subset of other
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        :return: String representation of the set
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        :return: More detailed string representation of the set
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """
        :return: Number of elements in the set
        """
        pass

    @abstractmethod
    def __contains__(self, item) -> bool:
        """
        :return: True if item is in the set, otherwise false
        """
        pass

    @abstractmethod
    def __add__(self, other: 'SetADT') -> 'SetADT':
        """
        :return: The union of two sets
        """
        pass

    @abstractmethod
    def __sub__(self, other: 'SetADT') -> 'SetADT':
        """
        :return: The difference of two sets
        """
        pass

    @abstractmethod
    def __eq__(self, other: 'SetADT') -> bool:
        """
        :return: True if two sets have the exact same elements, otherwise False
        """
        pass

    @abstractmethod
    def __ne__(self, other: 'SetADT') -> bool:
        """
        :return: False if two sets have the exact same elements, otherwise True
        """
        pass
