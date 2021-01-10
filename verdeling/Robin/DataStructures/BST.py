from typing import Callable, Optional, Tuple, TypedDict


class _BSTSave(TypedDict):
    root: int
    children: Tuple[Optional['_BSTSave'], Optional['_BSTSave']]


class BST:
    def __init__(self, root=None) -> None:
        self.root = root
        self.left: Optional['BST'] = None
        self.right: Optional['BST'] = None
        self.parent: Optional['BST'] = None

    def searchTreeInsert(self, newItem) -> bool:
        """
        voegt een item toe aan de BST
        :param newItem: object met getId() als functie, de searchKey is een getal.
        :return: Succes, geeft aan of de operatie geslaagd is.
        :pre newItem, of een item met hetzelfde SearchKey, zit nog niet in de BST
        :post newItem zit in de BST, de grootte van de BST is met 1 verhoogt.
        """
        if self.root is None:
            self.root = newItem
            return True

        if newItem.getId() < self.root.getId():
            if self.left is None:
                node = BST(newItem)
                node.parent = self
                self.left = node
                return True
            else:
                return self.left.searchTreeInsert(newItem)

        if newItem.getId() > self.root.getId():
            if self.right is None:
                node = BST(newItem)
                node.parent = self
                self.right = node
                return True
            else:
                return self.right.searchTreeInsert(newItem)

    def searchTreeRetrieve(self, searchKey: int) -> Tuple[Optional[object], bool]:
        """
        haalt het object met gegeven searchKey op uit de BST
        :param searchKey: een getal
        :return: geeft het (object, Succes) als het gevonden is in de BST, als het niet gevonden is dan geeft het (None, Succes) terug
        :pre geen
        :post De BST is niet veranderd
        """
        if searchKey == self.root.getId():
            return self.root, True

        if searchKey < self.root.getId():
            if self.left is not None:
                return self.left.searchTreeRetrieve(searchKey)
            else:
                return None, False

        else:
            if self.right is not None:
                return self.right.searchTreeRetrieve(searchKey)
            else:
                return None, False

    def __searchTreeRetrieve(self, searchKey: int) -> Tuple[Optional['BST'], bool]:
        """
        geeft het bst object terug met gegeven search key (private)
        :param searchKey: een getal
        :return: geeft het (object, Succes) als het gevonden is in de BST, als het niet gevonden is dan geeft het (None, Succes) terug
        :pre geen
        :post De BST is niet veranderd
        """
        if searchKey == self.root.getId():
            return self, True

        if searchKey < self.root.getId():
            if self.left is not None:
                return self.left.searchTreeRetrieve(searchKey)
            else:
                return None, False

        else:
            if self.right is not None:
                return self.right.searchTreeRetrieve(searchKey)
            else:
                return None, False

    def searchTreeDelete(self, searchKey: int) -> bool:
        """
        verwijdert de node met gegeven searchKey uit de BST
        :param searchKey: een getal
        :return: Succes
        :pre geen
        :post het item met searchKey zit niet meer in de BST, de grootte van de BST is met 1 vermindert.
        """
        node, found = self.__searchTreeRetrieve(searchKey)
        if not found:
            return False

        if not (node.left or node.right):
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None

        if node.left and node.right:
            node = node.__swap(node.__inorderSuccesor())
            if node.parent.left == node:
                node.parent.left = None

            elif node.parent.right == node:
                node.parent.right = None

            del node
            return True

        else:
            if node.left:
                child = node.left
            else:
                child = node.right

            node.root = child.root
            node.left = child.left
            node.right = child.right
            del child
            return True

    def __inorderSuccesor(self) -> Optional['BST']:
        """
        geeft de inorder succesor van een node terug, privé
        :return: inorder succesor node
        """
        if self.right is None:
            return None

        def left(node: 'BST') -> Optional['BST']:
            """
            zoekt het meest linkse kind
            :param node: Node
            :return: meest linkse Node
            """
            left_node: Optional['BST'] = node.left
            if left_node:
                left(left_node)
            else:
                return node

        return left(self.right)

    def __swap(self, other) -> 'BST':
        self.root = other.root
        return other

    def inorderTraverse(self, visit: Callable[[any], any], ) -> None:
        """
        overloopt de BST in inorder volgorde (van klein naar groot)
        :param visit functie die voor elke bezochte node word opgeroepen
        :return: None
        :pre geen
        :post de BST is onverandert
        """
        if not(self.left or self.right):
            visit(self.root.getId())
            return

        if self.left:
            self.left.inorderTraverse(visit)
        visit(self.root.getId())
        if self.right:
            self.right.inorderTraverse(visit)

    def isEmpty(self) -> bool:
        """
        :return: geeft terug of de BST leeg is (bool)
        """
        return self.root is None

    def save(self) -> _BSTSave:
        """
        slaagt de binaire zoekboom op in de vorm {root:root, children:[child1, child2]}
        :return: dict
        """
        save = {'root': self.root.getId()}
        if bool(self.left or self.right):
            save['children'] = [self.left.save() if self.left else None, self.right.save() if self.right else None]

        return save

    def load(self, tree: '_BSTSave') -> None:
        """
        slaagt de boom op in de vorm {root:root, children:[child1, child2]}
        :param tree: {root:root, children:[child1, child2]}
        :return: None
        """
        self.root = TreeItem(tree['root'], tree['root'])

        if 'children' in tree:
            if tree['children'][0]:
                left: BST = BST()
                left.load(tree['children'][0])
                self.left = left

            if tree['children'][1]:
                right: BST = BST()
                right.load(tree['children'][0])
                self.right = right


class TreeItem:
    def __init__(self, key, val):
        self.sk = key
        self.v = val

    def getId(self):
        return self.sk


def createTreeItem(key, val):
    return TreeItem(key, val)


if __name__ == "__main__":
    t = BST()
    print(t.isEmpty())
    print(t.searchTreeInsert(createTreeItem(8,8)))
    print(t.searchTreeInsert(createTreeItem(5,5)))
    print(t.isEmpty())
    print(t.searchTreeRetrieve(5))
    print(t.searchTreeRetrieve(5)[1])
    t.inorderTraverse(print)
    print(t.save())
    t.load({'root': 10,'children':[{'root':5},None]})
    t.searchTreeInsert(createTreeItem(15,15))
    print(t.searchTreeDelete(0))
    print(t.save())
    print(t.searchTreeDelete(10))
    print(t.save())
