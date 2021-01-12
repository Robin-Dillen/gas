from ..BST import BST
from typing import Tuple, Optional


class BSTTable:
    def __init__(self):
        self.__bst = BST()  # private

    def tableInsert(self, newItem) -> bool:
        """
        voegt een object toe aan de tabel
        :param newItem: object met getSearchKey() als functie, de searchKey is een getal.
        :return: Succes
        :pre newItem, of een item met hetzelfde SearchKey, zit nog niet in de tabel
        :post newItem zit in de tabel, de grootte van de tabel is met 1 verhoogt.
        """
        return self.__bst.searchTreeInsert(newItem)

    def tableDelete(self, searchKey: int) -> bool:
        """
        verwijdert de node met gegeven searchKey uit de tabel
        :param searchKey: een getal
        :return: Succes
        :pre geen
        :post het item met searchKey zit niet meer in de tabel, de grootte van de tabel is met 1 vermindert.
        """
        return self.__bst.searchTreeDelete(searchKey)

    def tableRetrieve(self, searchKey: int) -> Tuple[Optional[object], bool]:
        """
        haalt het object met gegeven searchKey op uit de tabel
        :param searchKey: een getal
        :return: geeft het (object, Succes) als het gevonden is in de tabel, als het niet gevonden is dan geeft het (None, Succes) terug
        :pre geen
        :post De tabel is niet veranderd
        """
        return self.__bst.searchTreeRetrieve(searchKey)

    def traverseTable(self, visit: any) -> None:
        """
        overloopt de tabel in volgorde, van klein naar groot
        :return: een tuple met de elementen in, van eerst naar laatste element
        :pre geen
        :post de tabel is onverandert
        """
        return self.__bst.inorderTraverse(visit)

    def tableIsEmpty(self):
        """
        Geeft terug of de tabel leeg is
        :return: bool
        """
        return self.__bst.isEmpty()

    def tableLength(self):
        """geeft de grootte van de boom terug"""
        return self.__bst.getSize()

    def save(self):
        """
        slaagt het object op in een dict in de vorm {root:root, children:[child1, child2]}
        :return: een dict
        """
        return self.__bst.save()

    def load(self, tree):
        """
        laadt een boom in, in dict vorm: {root:root, children:[child1, child2]}
        :param tree: {root:root, children:[child1, child2]}
        :return: None
        """
        self.__bst.load(tree)


class TreeItem:
    def __init__(self, key, val):
        self.sk = key
        self.v = val

    def getSearchKey(self):
        return self.sk


def createTreeItem(key, val):
    return TreeItem(key, val)


if __name__ == "__main__":
    t = BSTTable()
    print(t.tableIsEmpty())
    print(t.tableInsert(createTreeItem(8,8)))
    print(t.tableInsert(createTreeItem(5,5)))
    print(t.tableIsEmpty())
    print(t.tableRetrieve(5)[0])
    print(t.tableRetrieve(5)[1])
    t.traverseTable(print)
    print(t.save())
    t.load({'root': 10,'children':[{'root':5},None]})
    t.tableInsert(createTreeItem(15,15))
    print(t.tableDelete(0))
    print(t.save())
    print(t.tableDelete(10))
    print(t.save())