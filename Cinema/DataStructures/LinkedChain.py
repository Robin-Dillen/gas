from typing import NoReturn, Optional, Tuple, TypeVar
from Cinema.BuildingBlocks import _Foundation

_ItemType = TypeVar("_ItemType", bound=_Foundation)


class LinkedChain:
    def __init__(self):
        self.head: Dummy = Dummy() # private
        self.size: int = 0 # private

    def isEmpty(self) -> bool:
        """
        :return: geeft True terug als de gelinkte ketting leeg is, anders False
        :pre geen
        :post de gelinkte ketting is niet aangepast
        """
        return self.size == 0

    def getLength(self) -> int:
        """
        :return: geeft de lengte van de gelinkte ketting terug
        :pre geen
        :post de gelinkte ketting is niet aangepast
        """
        return self.size

    def retrieve(self, index: int) -> Tuple[Optional[_ItemType], bool]:
        """
        geeft het object op plaats index terug
        :param index: positieve int < de lengte van de linked chain
        :return: object, True als het geslaagd is
        """
        if not(1 <= index <= self.size):
            return None, False

        node: 'Node' = self.head
        for _ in range(index):
            node: 'Node' = node.getNext()

        return node.getData(), True

    def __retrieve(self, index: int) -> Tuple[Optional['Node'], bool]:
        """
        geeft de node op plaats index terug, private functie
        :return: Node
        """
        if not(0 <= index <= self.size):
            return None, False

        node: 'Node' = self.head
        for _ in range(index):
            node: 'Node' = node.getNext()

        return node, True

    def insert(self, index: int, data) -> bool:
        """
        voegt een object toe op een bepaalde plek in de lijst
        :param object: object dat geïnsert moet worden
        :param index: positieve int <= de lengte van de linked chain, duidt aan waar het element toegevoegt moet worden
        :return: Success
        :pre geen
        :post als het toevoegen is gelukt dan zit object op plaats index in de gelinkte ketting, en wordt er True teruggeven.
        alle elementen met een index, groter dan de gegeven index zijn 1 plaatsje naar rechts opgeschoven.
        Als het toevoegen mislukt is wordt er False teruggegeven.
        """
        node, succes = self.__retrieve(index - 1)
        if not succes:
            return False
        newNode = Node(data)
        newNode.setPrevious(node)
        newNode.setNext(node.getNext())
        node.setNext(newNode)
        newNode.getNext().setPrevious(newNode)
        self.size += 1
        return True

    def delete(self, index: int) -> bool:
        """
        verwijdert het object op een bepaalde plaats
        :param index: positieve int < de lengte van de linked chain, duidt aan op welke plaats het element zit dat verwijdert moet worden
        :return: Succes
        :pre geen
        :post als het verwijderen gelukt is dan bevind het object zich niet meer in de linked chain, alle objecten die rechts van het verwijderde
        object zaten zijn 1 plaatsje naar links opgeschoven
        """
        node, found = self.__retrieve(index)
        if not found or type(node) is Dummy:
            return False

        node.getPrevious().setNext(node.getNext())
        node.getNext().setPrevious(node.getPrevious())
        del node
        self.size -= 1
        return True

    def traverse(self, visit, next=None):
        """
        bezoekt elke node
        :param visit: func
        :return: None
        """
        if next.getNext() == self.head:
            return
        if not next:
            next = self.head
        visit(next.getNext())
        self.traverse(visit, next.getNext())

    def save(self) -> list:
        """
        slaagt de gelinkte ketting op als een lijst
        :return: lijst
        """
        save = []
        node = self.head.getNext()
        for _ in range(self.size):
            save.append(node.getData())
            node = node.getNext()

        return save

    def load(self, load: list) -> None:
        """
        slaagt de gelinkte ketting op in een lijst
        :param load: lijst
        :return: None
        """
        self.__cleanup()
        for node in load:
            self.insert(self.size + 1, node)

    def __cleanup(self) -> None:
        """
        prive functie dat alle nodes, behalve de dummy node, verwijdert en de size naar 0 zet
        :return: None
        :pre geen
        :post er zitten geen nodes meer in de linked chain (behalve de dummy node) en de size is 0
        """
        for index in range(self.size):
            self.delete(index)
        self.size = 0


class Node:
    def __init__(self, obj: Optional[_ItemType] = None):
        self.__data: Optional[_ItemType] = obj  # private
        self.__previous: Optional['Node'] = None  # private
        self.__next: Optional['Node'] = None  # private

    def setNext(self, node: 'Node') -> bool:
        """
        zet de pointer naar de volgende node
        :param node: volgende node, node is een Node object
        :return: Succes
        :pre geen
        :post de pointer naar de volgende node is aangepast
        """
        self.__next = node
        return True

    def getNext(self) -> 'Node':
        """
        geeft een pointer naar de volgende node terug
        :return: node
        :pre geen
        :post
        """
        return self.__next

    def setPrevious(self, node: 'Node') -> bool:
        """
        zet de pointer naar de vorige node
        :param node: vorige node, node is een Node object
        :return: Succes
        :pre geen
        :post de pointer naar de vorige node is aangepast
        """
        self.__previous = node
        return True

    def getPrevious(self) -> 'Node':
        """
        geeft een pointer naar de vorige node terug
        :return: Node
        :pre geen
        :post
        """
        return self.__previous

    def getData(self) -> Optional[_ItemType]:
        """
        geeft de data van de node terug
        :return: data
        :pre geen
        :post geen
        """
        return self.__data


class Dummy(Node):
    def __init__(self):
        super().__init__()
        self.setNext(self)
        self.setPrevious(self)

    def getData(self) -> NoReturn:
        raise NotImplementedError('Dummy head node has no data!')


if __name__ == "__main__":
    l = LinkedChain()
    print(l.isEmpty())    # True
    print(l.getLength())    # 0
    print(l.retrieve(4)[1])    # False
    print(l.insert(4, 500))    # False
    print(l.isEmpty())    # True
    print(l.insert(1, 500))    # True
    print(l.retrieve(1)[0])    # 500
    print(l.retrieve(1)[1])    # True
    print(l.save())    # [500]
    print(l.insert(1, 600))    # True
    print(l.save())    # [600, 500]
    l.load([10, -9, 15])
    l.insert(3, 20)
    print(l.delete(0))    # False
    print(l.save())    # [10, -9, 20, 15]
    print(l.delete(1)) # True
    print(l.save()) # [-9, 20, 15]

