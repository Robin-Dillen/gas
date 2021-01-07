from Cinema.DataStructures.RedBlackTree import RedBlackTree, _TreeItemType
from typing import Tuple, Optional


class RedBlackTreeTable:
    def __init__(self):
        self.__rbt = RedBlackTree()  # private

    def tableInsert(self, newItem):
        """
        voegt een object toe aan de tabel
        :param newItem: object met getSearchKey() als functie, de searchKey is een getal.
        :return: Succes
        :pre newItem, of een item met hetzelfde SearchKey, zit nog niet in de tabel
        :post newItem zit in de tabel, de grootte van de tabel is met 1 verhoogt.
        """
        return self.__rbt.insertItem(newItem)

    def tableDelete(self, searchKey: int) -> bool:
        """
        verwijdert de node met gegeven searchKey uit de tabel
        :param searchKey: een getal
        :return: Succes
        :pre geen
        :post het item met searchKey zit niet meer in de tabel, de grootte van de tabel is met 1 vermindert.
        """
        return self.__rbt.deleteItem(searchKey)

    def tableRetrieve(self, searchKey: int) -> Tuple[Optional[_TreeItemType], bool]:
        """
        haalt het object met gegeven searchKey op uit de tabel
        :param searchKey: een getal
        :return: geeft het (object, Succes) als het gevonden is in de tabel, als het niet gevonden is dan geeft het (None, Succes) terug
        :pre geen
        :post De tabel is niet veranderd
        """
        return self.__rbt.retrieveItem(searchKey)

    def traverseTable(self, visit: any) -> None:
        """
        overloopt de tabel in volgorde, van klein naar groot
        :return: een tuple met de elementen in, van eerst naar laatste element
        :pre geen
        :post de tabel is onverandert
        """
        return self.__rbt.inorderTraverse(visit)

    def tableIsEmpty(self):
        """
        Geeft terug of de tabel leeg is
        :return: bool
        """
        return self.__rbt.isEmpty()

    def save(self):
        """
        slaagt het object op in een dict in de vorm {root:root, color:color, children:[child1, child2]}
        :return: een dict
        """
        return self.__rbt.save()

    def load(self, tree):
        """
        laadt een boom in, in dict vorm: {root:root, color:color, children:[child1, child2]}
        :param tree: {root:root, color:color, children:[child1, child2]}
        :return: None
        """
        self.__rbt.load(tree)