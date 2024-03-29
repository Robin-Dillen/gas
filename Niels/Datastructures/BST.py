def createTreeItem(key, val):
    return val


class BST:
    def __init__(self, key=None, parent=None, value=None):
        self.root = key
        self.value = value
        self.LeftTree = None
        self.RightTree = None
        self.parent = parent


    def load(self, tree):
        """
        Laadt een binaire zoekboom in
        :param tree: string vorm van boom met items
        :return: /
        preconditie:/

        postconditie:/
        """
        if (tree == None):
            self.root = None
        else:
            self.root = tree['root']
        self.LeftTree = None
        self.RightTree = None
        self.parent = None
        self.value = None
        if (tree.getLength == 2):
            if (tree['children'][0] != None):
                self.LeftTree = BST()
                self.LeftTree.load(tree['children'][0])
                self.LeftTree.parent = self
            if (tree['children'][1] != None):
                self.RightTree = BST()
                self.RightTree.load(tree['children'][1])
                self.RightTree.parent = self
        return

    def searchTreeInsert(self, value):
        """
        voegt een item toe aan de boom
        :param object: waarde van het item (tuple)
        :return: none
        precondition: None

        postcondition: None
        """
        if (self.root == None):
            self.root = value.getId()
            self.value = value
        elif (self.LeftTree == None and value.getId() < self.root):
            nieuwe_knoop = BST(value.getId(), None, value)
            nieuwe_knoop.parent = self
            self.LeftTree = nieuwe_knoop
        elif (self.RightTree == None and value.getId() > self.root):
            nieuwe_knoop = BST(value.getId(), None, value)
            nieuwe_knoop.parent = self
            self.RightTree = nieuwe_knoop
        elif (self.LeftTree != None and value.getId() < self.root):
            self.LeftTree.searchTreeInsert(value)
        elif (self.RightTree != None and value.getId() > self.root):
            self.RightTree.searchTreeInsert(value)
        return True

    def __zoekinordersuccessor(self, right=True):
        """
        Zoekt de inorder successor van een item
        :param right: Geeft aan of de recursieve functie al naar rechts is gesprongen of niet
        :return: De inorder succesor van een item
        precondition: het item mag geen blad zijn

        postcondition: None
        """
        if (right == False):
            if (self.LeftTree == None):
                return self
            else:
                return (self.LeftTree.zoekinordersuccessor(False))
        else:
            return (self.RightTree.zoekinordersuccessor(False))

    def searchTreeDelete(self, key):
        """
        verwijdert een item
        :param key: waarde van het item
        :return: none

        precondition: None

        postcondition: None
        """

        if (self.root == key):
            if (self.parent != None):
                if (self.LeftTree == None and self.RightTree == None):
                    if (self.parent.root < self.root):
                        self.parent.RightTree = None
                        self.root = None
                        self.value = None
                    elif (self.parent.root > self.root):
                        self.parent.LeftTree = None
                        self.root = None
                        self.value = None
                elif (self.LeftTree != None and self.RightTree != None):
                    inorder = self.__zoekinordersuccessor()
                    inorder.parent.LeftTree = None
                    self.root = inorder.root
                    self.value = inorder.value
                    inorder.searchTreeDelete(inorder.root)
                    if (self.parent.root < self.root):
                        self.parent.RightTree = self.root
                    elif (self.parent.root > self.root):
                        self.parent.LeftTree = self.root
                elif (self.LeftTree != None and self.RightTree == None):
                    self.parent.LeftTree = self.LeftTree
                    self.root = None
                    self.value = None
                elif (self.LeftTree == None and self.RightTree != None):
                    self.parent.RightTree = self.RightTree
                    self.root = None
                    self.value = None
            elif (self.parent == None):
                if (self.LeftTree == None and self.RightTree == None):
                    self.root = None
                    self.value = None
                elif (self.LeftTree != None and self.RightTree != None):
                    inorder = self.__zoekinordersuccessor()
                    if (self.RightTree.LeftTree == None):
                        inorder.parent.RightTree = None
                    else:
                        inorder.parent.LeftTree = None
                    self.root = inorder.root
                    self.value = inorder.value
                    inorder.searchTreeDelete(inorder.root)
                elif (self.LeftTree != None and self.RightTree == None):
                    self.LeftTree.parent = None
                    self.root = None
                    self.value = None
                elif (self.LeftTree == None and self.RightTree != None):
                    self.RightTree.parent = None
                    self.root = None
                    self.value = None
            return True
        elif (self.root < key and self.RightTree != None):
            self.RightTree.searchTreeDelete(key)
        elif (self.root > key and self.LeftTree != None):
            self.LeftTree.searchTreeDelete(key)
        return False

    def inorderTraverse(self, prnt = None):
        """
        Doorloopt een boom en print deze uit
        :param ptnt: Geeft aan of het geprint moet worden of niet
        :return: True als het gelukt is

        precondition: None

        postcondition: None
        """
        if (prnt):
            if (self.LeftTree != None):
                self.LeftTree.inorderTraverse(prnt)
            prnt(self.value)
            if (self.RightTree != None):
                self.RightTree.inorderTraverse(prnt)
            return True
        else:
            return False

    def getDepth(self, hoogte=0):
        """
        geeft de diepte van de boom terug
        :return: diepte van de boom

        precondition: None

        postcondition: None
        """
        if (self.root == None):
            return hoogte
        elif (self.LeftTree == None and self.RightTree == None):
            return hoogte + 1
        elif (self.LeftTree == None and self.RightTree != None):
            hoogte = self.RightTree.getdepth(hoogte) + 1
        elif (self.LeftTree != None and self.RightTree == None):
            hoogte = self.LeftTree.getdepth(hoogte) + 1
        elif (self.RightTree.getdepth() > self.LeftTree.getdepth()):
            hoogte = self.RightTree.getdepth(hoogte) + 1
        elif (self.RightTree.getdepth() <= self.LeftTree.getdepth()):
            hoogte = self.LeftTree.getdepth(hoogte) + 1
        return hoogte

    def getLength(self, lengte=0):
        """
        geeft het aantal knopen van de boom terug
        :return: aantal knopen van de boom

        precondition: None

        postcondition: None
        """
        if (self.root == None):
            return lengte
        elif (self.LeftTree == None and self.RightTree == None):
            return lengte + 1
        elif (self.LeftTree != None and self.RightTree == None):
            return lengte + self.LeftTree.getlength() + 1
        elif (self.LeftTree == None and self.RightTree != None):
            return lengte + self.RightTree.getlength() + 1
        return (self.LeftTree.getlength() + self.RightTree.getlength() + lengte + 1)

    def isEmpty(self):
        """
        Kijkt na of een boom leeg is of niet
        :return: True als het leeg is, false als het niet leeg is
        precondition: None

        postcondition: None
        """
        if (self.value == None):
            return True
        else:
            return False

    def searchTreeRetrieve(self, id):
        if(self.value != None):
            if (self.value.getId() == id):
                return self.value, True
            elif (self.value.getId() > id and self.LeftTree != None):
                return self.LeftTree.searchTreeRetrieve(id)
            elif (self.value.getId() < id and self.RightTree != None):
                return self.RightTree.searchTreeRetrieve(id)
        return None, False


    def save(self):
        """
        slaat de boom correct op
        :return: dictionary van de boom

        precondition: None

        postcondition: None
        """
        if (self.LeftTree == None and self.RightTree == None):
            return {'root': self.value.getId()}
        elif (self.LeftTree != None and self.RightTree == None):
            return {'root': self.value.getId(), 'children': [self.LeftTree.save(), None]}
        elif (self.LeftTree == None and self.RightTree != None):
            return {'root': self.value.getId(), 'children': [None, self.RightTree.save()]}
        return {'root': self.value.getId(), 'children': [self.LeftTree.save(), self.RightTree.save()]}


class BSTTable:
    def __init__(self):
        self.a = BST()

    def load(self, tree):
        self.a.load(tree)

    def tableInsert(self,value):
        return self.a.searchTreeInsert(value)

    def tableDelete(self, key):
        return self.a.searchTreeDelete(key)

    def tableLength(self):
        return self.a.getLength()

    def tableIsEmpty(self):
        return self.a.isEmpty()

    def traverseTable(self, key = None):
        return self.a.inorderTraverse(key)

    def tableRetrieve(self, key):
        return self.a.searchTreeRetrieve(key)

    def save(self):
        return self.a.save()


if __name__ == "__main__":
    t = BST()
    print(t.isEmpty())
    print(t.searchTreeInsert(createTreeItem(8, 8)))
    print(t.searchTreeInsert(createTreeItem(5, 5)))
    print(t.isEmpty())
    print(t.searchTreeRetrieve(5)[0])
    print(t.searchTreeRetrieve(5)[1])
    t.inorderTraverse(print)
    print(t.save())
    t.load({'root': 10, 'children': [{'root': 5}, None]})
    t.searchTreeInsert(createTreeItem(15, 15))
    print(t.searchTreeDelete(0))
    print(t.save())
    print(t.inorderTraverse())
    print(t.inorder_succ(10))
    print(t.searchTreeDelete(10))
    print(t.save())

    t = BSTTable()
    print(t.tableIsEmpty())
    print(t.tableInsert(createTreeItem(8, 8)))
    print(t.tableInsert(createTreeItem(5, 5)))
    print(t.tableIsEmpty())
    print(t.tableRetrieve(5)[0])
    print(t.tableRetrieve(5)[1])
    t.traverseTable(print)
    print(t.save())
    t.load({'root': 10, 'children': [{'root': 5}, None]})
    t.tableInsert(createTreeItem(15, 15))
    print(t.tableDelete(0))
    print(t.save())
    print(t.tableDelete(10))
    print(t.save())