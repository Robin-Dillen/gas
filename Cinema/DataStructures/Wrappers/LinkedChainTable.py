from Cinema.DataStructures.LinkedChain import LinkedChain
from Cinema.BuildingBlocks import _Foundation
from typing import TypeVar, Union, Tuple, Optional

_ItemType = TypeVar("_ItemType", bound=_Foundation)


class LinkedChainTable:
    def __init__(self):
        self.__linked_chain = LinkedChain()  # private

    def tableInsert(self, index: int, newItem: _ItemType):
        """
        voegt een object toe aan de tabel
        :param newItem: object met getSearchKey() als functie, de searchKey is een getal.
        :return: Succes
        :pre newItem, of een item met hetzelfde SearchKey, zit nog niet in de tabel
        :post newItem zit in de tabel, de grootte van de tabel is met 1 verhoogt.
        """
        return self.__linked_chain.insert(index, newItem)

    def tableDelete(self, index):
        """
        verwijdert de node met gegeven searchKey uit de tabel
        :param searchKey: een getal
        :return: Succes
        :pre geen
        :post het item met searchKey zit niet meer in de tabel, de grootte van de tabel is met 1 vermindert.
        """
        return self.__linked_chain.delete(index)

    def tableRetrieve(self, index: int) -> Tuple[Optional[_ItemType], bool]:
        """
        haalt het object met gegeven index op uit de tabel
        :param index: een getal
        :return: geeft het (object, Succes) als het gevonden is in de tabel, als het niet gevonden is dan geeft het (None, Succes) terug
        :pre geen
        :post De tabel is niet veranderd
        """
        return self.__linked_chain.retrieve(index)

    def traverseTable(self) -> tuple:
        """
        overloopt elk element van de tabel, in volgorde van toevoeging.
        :return: een tuple met de elementen in
        :pre geen
        :post de tabel is onverandert
        """
        objs = []
        for i in range(self.__linked_chain.getLength() - 1):
            objs.append(self.__linked_chain.retrieve(i))

        return tuple(objs)

    def tableIsEmpty(self) -> bool:
        """
        geeft terug of de tabel leeg is
        :return: bool
        """
        return self.__linked_chain.isEmpty()

    def tableLength(self) -> int:
        """
        geeft de grootte van de tabel terug
        :return: int
        """
        return self.__linked_chain.getLength()

    def save(self) -> list:
        """
        slaagt het object op in een lijst
        :return: een lijst
        """
        return self.__linked_chain.save()

    def load(self, l: list):
        """
        laadt een lijst in
        :param l: list
        :return: None
        """
        self.__linked_chain.load(l)

