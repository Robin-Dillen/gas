from typing import TypeVar, TypedDict, Tuple, Optional, Union


class _BSTSave(TypedDict):
    root: int
    children: Tuple[Optional['_BSTSave'], Optional['_BSTSave']]


class RedBlackTree:
    """naar idee van https://en.wikipedia.org/wiki/Red%E2%80%93black_tree (insert en delete)"""
    def __init__(self, root: Optional[object] = None):
        self.root: Optional[object] = root
        self.color: bool = True  # False is black, red is True
        self.left: Optional[RedBlackTree] = None
        self.right: Optional[RedBlackTree] = None
        self.parent: Optional[RedBlackTree] = None

    def insertItem(self, newItem: object) -> bool:
        """
        voegt een item toe aan de RBT
        :param newItem: object met getId() als functie, de searchKey is een getal.
        :return: Succes, geeft aan of de operatie geslaagd is.
        :pre newItem, of een item met hetzelfde SearchKey, zit nog niet in de RBT
        :post newItem zit in de RBT, de grootte van de RBT is met 1 verhoogt.
        """
        newNode = self.insertRecurse(newItem)
        newNode.__insertRepairTree()
        return True

    def insertRecurse(self, newItem: object) -> 'RedBlackTree':
        """
        zoekt het juiste blad recursief en steekt het nieuwe item in dat blad
        :param newItem: item dat geïnsert moet worden
        :return: None
        :pre geen
        :post het nieuwe item zit in de boom
        """
        if self.root is None:
            self.root = newItem
            self.color = True
            return self

        if newItem.getId() < self.root.getId():
            if self.left is None:
                child: RedBlackTree = RedBlackTree(newItem)
                child.parent = self
                self.left = child
                return child

            return self.left.insertRecurse(newItem)

        if newItem.getId() > self.root.getId():
            if self.right is None:
                child: RedBlackTree = RedBlackTree(newItem)
                child.parent = self
                self.right = child
                return child

            return self.right.insertRecurse(newItem)

    def __insertRepairTree(self) -> None:
        """
        balanceert de boom nadat er een insert is gedaan
        :return: None
        :pre: de boom is niet gebalanceert
        :post: de boom is gebalanceert
        """
        if self.parent is None:
            self.__insertCase1()
            return
        if self.parent.color is False:
            return
        if self.uncle is not None and self.uncle.color is True:
            self.__insertCase2()
            return
        self.__insertCase3()

    def __insertCase1(self) -> None:
        """zet de kleur naar zwart"""
        self.color = False

    def __insertCase2(self) -> None:
        """kleuren veranderen en recursieve aanroep naar repair tree"""
        self.parent.color = False
        self.uncle.color = False
        self.grandparent.color = True
        self.grandparent.__insertRepairTree()

    def __insertCase3(self) -> None:
        """rotaties en herkleuringen"""
        if self == self.parent.right and self.parent == self.grandparent.left:
            self.parent.__rotateLeft()
            self.left.__insertCase3Step2()
        elif self == self.parent.left and self.parent == self.grandparent.right:
            self.parent.__rotateRight()
            self.right.__insertCase3Step2()

    def __insertCase3Step2(self) -> None:
        """rotaties en herkleuringen"""
        if self == self.parent.left:
            self.grandparent.__rotateRight()
        else:
            self.grandparent.__rotateLeft()

        self.parent.color = False
        self.grandparent.color = True

    def __rotateLeft(self) -> None:
        """
        draait node naar links
        :return: None
        """
        child = self.right
        self.root, child.root = child.root, self.root
        self.right = child.right
        child.right = child.left
        child.left = self.left
        self.left = child

    def __rotateRight(self) -> None:
        """
        draait de nodes naar rechts
        :return: None
        """
        child = self.right
        self.root, child.root = child.root, self.root
        self.right = child.right
        child.right = child.left
        child.left = self.left
        self.left = child

    def retrieveItem(self, searchKey: int) -> Tuple[Optional[object], bool]:
        """
        haalt het object met gegeven searchKey op uit de RBT
        :param searchKey: een getal
        :return: geeft het (object, Succes) als het gevonden is in de RBT, als het niet gevonden is dan geeft het (None, Succes) terug
        :pre geen
        :post De RBT is niet veranderd
        """
        if searchKey == self.root.getId():
            return self.root.getId(), True

        elif searchKey < self.root.getId():
            if self.left is None:
                return None, False
            return self.left.retrieveItem(searchKey)

        if self.right is None:
            return None, False
        return self.right.retrieveItem(searchKey)

    def __retrieveItem(self, searchKey: int) -> Optional['RedBlackTree']:
        """
        haalt het object met gegeven searchKey op uit de RBT
        :param searchKey: een getal
        :return: geeft het (object, Succes) als het gevonden is in de RBT, als het niet gevonden is dan geeft het (None, Succes) terug
        :pre geen
        :post De RBT is niet veranderd
        """
        if searchKey == self.root.getId():
            return self

        elif searchKey < self.root.getId():
            if self.left is None:
                return None
            return self.left.__retrieveItem(searchKey)

        if self.right is None:
            return None
        return self.right.__retrieveItem(searchKey)

    def deleteItem(self, searchKey: int) -> bool:
        """
        verwijdert de node met gegeven searchKey uit de RBT
        :param searchKey: een getal
        :return: Succes
        :pre geen
        :post het item met searchKey zit niet meer in de RBT, de grootte van de RBT is met 1 vermindert.
        """
        node = self.__retrieveItem(searchKey)
        if node is None:
            return False
        if not (node.left or node.right):  # no children
            node.parent.__deleteCase1()
            if node.parent.left == node:
                node.parent.left = None
                node.parent.__rotateLeft()
            else:
                node.parent.right = None
                node.parent.__rotateRight()

            return True

        if not (node.left and node.right):  # 1 child
            node.__deleteOneChild(searchKey)

        else:
            node.__delete2children(searchKey)

        return True

    def __delete2children(self, searchKey: int) -> None:
        """delete als de node 2 kinderen heeft, __switch met innorder succesor"""
        node = self.__switch(self.__inorderSuccesor())
        node.deleteItem(searchKey)

    def __deleteOneChild(self, searchKey:int) -> None:
        """delete case, 1 kind"""
        if self.left:
            child = self.__switch(self.left)
        else:
            child = self.__switch(self.right)

        if self.color is False:
            if child.color is True:
                child.color = False
                if self.left == child:
                    self.left = None

                else:
                    self.right = None

            else:
                child.__deleteCase1()

    def __switch(self, node) -> 'RedBlackTree':
        """switched 2 nodes om, geeft de nieuwe node terug"""
        self.root, node.root = node.root, self.root
        return node

    def __deleteCase1(self) -> None:
        if self.parent is not None:
            self.__deleteCase2()

    def __deleteCase2(self) -> None:
        if self.sibling.color is True:
            self.parent.color = True
            self.sibling.color = False
            if self == self.parent.left:
                self.parent.__rotateLeft()
            else:
                self.parent.__rotateRight()
        self.__deleteCase3()

    def __deleteCase3(self) -> None:
        if self.parent.color is False and self.sibling.color is False and self.left.color is False and self.right.color is False:
            self.color = True
            self.parent.__deleteCase1()
        else:
            self.__deleteCase4()

    def __deleteCase4(self) -> None:
        if self.parent.color is True and self.sibling.color is False and self.sibling.left.color is False and self.sibling.right.color is False:
            self.sibling.color = True
            self.parent.color = False
        else:
            self.__deleteCase5()

    def __deleteCase5(self) -> None:
        if self.sibling.color is False:
            if self == self.parent.left and self.sibling.right.color is False and self.sibling.left.color is True:
                self.sibling.color = True
                self.sibling.left.color = False
                self.sibling.__rotateRight()
            elif self == self.parent.right and self.sibling.left.color is False and self.sibling.right is False:
                self.sibling.color = True
                self.sibling.right.color = False
                self.sibling.__rotateLeft()
        self.__deleteCase6()

    def __deleteCase6(self) -> None:
        self.sibling.color = self.parent.color
        self.parent.color = False

        if self == self.parent.left:
            self.sibling.right.color = False
            self.parent.__rotateLeft()
        else:
            self.sibling.color = False
            self.parent.__rotateRight()

    def __inorderSuccesor(self) -> Optional['RedBlackTree']:
        """
        geeft de inorder succesor van de node terug.
        :return: inorder succesor
        """
        if self.right is None:
            return None

        def left(node):
            if node.left is not None:
                left(node.left)

            return node

        return left(self.right)

    def inorderTraverse(self, visit) -> None:
        """
        overloopt de RBT in inorder volgorde (van klein naar groot), past de visit functie toe op de nodes
        :return: een tuple met de elementen in, van eerst naar laatste element
        :pre geen
        :post de RBT is onverandert
        """
        if not (self.left or self.right):
            visit(self.root.getId())
            return

        if self.left:
            self.left.inorderTraverse(visit)
        visit(self.root.getId())
        if self.right:
            self.right.inorderTraverse(visit)

    def isEmpty(self) -> bool:
        """
        :return: geeft terug of de RBT leeg is (bool)
        """
        return self.root is None

    def save(self) -> _BSTSave:
        save = {'root': self.root.getId(), 'color': 'red' if self.color else 'black'}
        if bool(self.left or self.right):
            save['children'] = [self.left.save() if self.left else None, self.right.save() if self.right else None]

        return save

    def load(self, tree: '_BSTSave') -> None:
        """
        slaagt de boom op in de vorm {root:root, color:color, children:[child1, child2]}
        :param tree: {root:root, color:color, children:[child1, child2]}
        :return: None
        """
        self.clear()
        self.__loadItems(tree)

    def __loadItems(self, tree: Union['_BSTSave', list]) -> None:
        """
        laadt de items in de boom
        :param tree: dict/list van de boom
        :return: None
        """

        self.root = TreeItem(tree['root'], tree['root'])  # TreeItem is for testing purposes
        self.color = False if tree["color"] == "black" else True

        if 'children' in tree:
            if tree['children'][0]:
                self.left = RedBlackTree()
                self.left.loadItems(tree['children'][0])

            if tree['children'][1]:
                self.right = RedBlackTree()
                self.right.loadItems(tree['children'][1])

    def clear(self) -> None:
        """maakt de boom leeg"""
        self.root = None
        self.left = None
        self.right = None
        self.parent = None

    @property
    def grandparent(self) -> Optional['RedBlackTree']:
        """
        geeft de grootvader terug
        :return: grandparent, als diet bestaat anders None
        :precondities: geen
        :postconditites: geen
        """
        if self.parent is None:
            return None
        return self.parent.parent

    @grandparent.setter
    def grandparent(self, val: Optional['RedBlackTree']) -> None:
        """
        zet de waarde van de grootvader
        :param val: waarde
        :return: None
        :precondities: geen
        :postconditites: geen
        """
        self.parent.parent = val

    @property
    def uncle(self) -> Optional['RedBlackTree']:
        """
        geeft de waarde van de nonkel terug
        :return: uncle, als diet bestaat anders None
        :precondities: geen
        :postconditites: geen
        """
        if self.grandparent is None:
            return None
        return self.grandparent.left if self.grandparent.left != self.parent else self.grandparent.right

    @property
    def sibling(self) -> Optional['RedBlackTree']:
        if self.parent is None:
            return None
        if self == self.parent.left:
            if self.parent.right is not None:
                return self.parent.right
            return None
        elif self.parent.left is not None:
            return self.parent.left


class TreeItem:
    def __init__(self, key, val):
        self.sk = key
        self.v = val

    def getSearchKey(self):
        return self.sk


def createTreeItem(key, val):
    return TreeItem(key, val)


if __name__ == "__main__":
    t = RedBlackTree()
    print(t.isEmpty())
    print(t.insertItem(createTreeItem(8,8)))
    print(t.insertItem(createTreeItem(5,5)))
    print(t.insertItem(createTreeItem(10,10)))
    print(t.insertItem(createTreeItem(15,15)))
    print(t.isEmpty())
    print(t.retrieveItem(5)[0])
    print(t.retrieveItem(5)[1])
    t.inorderTraverse(print)
    print(t.save())
    t.load({'root': 8,'color': 'black','children':[{'root':5,'color': 'black'},{'root':10,'color': 'black'}]})
    t.insertItem(createTreeItem(15,15))
    print(t.deleteItem(0))
    print(t.save())
    print(t.deleteItem(10))
    print(t.save())

    """
True
True
True
True
True
False
5
True
5
8
10
15
{'root': 8,'color': 'black','children':[{'root':5,'color': 'black'},{'root':10,'color': 'black','children':[None,{'root':15,'color': 'red'}]}]}
False
{'root': 8,'color': 'black','children':[{'root':5,'color': 'black'},{'root':10,'color': 'black','children':[None,{'root':15,'color': 'red'}]}]}
True
{'root': 8,'color': 'black','children':[{'root':5,'color': 'black'},{'root':15,'color': 'black'}]}
"""
