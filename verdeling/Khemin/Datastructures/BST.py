def createTreeItem(key, val):
    return (key, val)

###Een klasse als voorstelling voor een binaire zoekboom.
class BST():
    # Initialiseert een nieuwe BST. N geeft het aantal elementen in een knoop weer (voor een binaire
    # zoekboom is dit steeds 1), root is de wortel van de BST en de zoeksleutel van het object dat in
    # het value atribuut wordt bewaard. Het leftChild vormt de linkerdeelboom en al zijn elementen zijn kleiner dan de
    # root. Het rightChild vormt de rechtedeelboom en al zijn elementen zijn groter dan de root. Beide deelbomen zijn
    # opnieuw objecten van de klasse BST. Het parent atribuut geeft weer wie de ouder is van de
    # BST. Voor de wortel van een BST is dit None.
    #
    # pre: De eventueel meegegeven parent is een BST.
    def __init__(self, parent=None):
        self.N = 1
        self.root = None
        self.value = None
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

    # Een methode die weergeeft of een BST leeg is of niet.
    #
    # return: True als de boom leeg is, anders False.
    def isEmpty(self):
        if self.root is None and self.leftChild is None and self.rightChild is None and self.value is None:
            return True
        else:
            return False

    # Een methode die de hoogte van de BST teruggeeft als een integer.
    #
    # return: De hoogte van de BST wordt teruggegeven als een integer.
    def hoogte(self):

        if self.leftChild is None and self.rightChild is None:
            return 1

        if self.leftChild is None:
            return 1 + self.rightChild.hoogte()

        if self.rightChild is None:
            return 1 + self.leftChild.hoogte()

        else:
            return max(1 + self.leftChild.hoogte(), 1 + self.rightChild.hoogte())

    # Een methode die de zoeksleutel van het grootste element in de BST teruggeeft.
    #
    # return: De grootste zoeksleutel in de BST wordt teruggegeven indien er een grootste zoeksleutel
    # bestaat. None wordt teruggegeven als de BST leeg is.
    def largest_key(self):
        if self.isEmpty():
            return None
        elif self.rightChild is None:
            return self.root
        else:
            return self.rightChild.largest_key()

    # Een methode die de BST doorloopt op zoek naar het gegeven item en geeft terug adv een booleaanse
    # waarde of het item gevonden werd of niet.
    #
    # return: True indien het item in de BST aanwezig is, anders False.
    def searchTreeSearch(self, item):
        if self.root != item and self.leftChild is None and self.rightChild is None:
            return False
        elif self.root != item and self.leftChild is None and item < self.root:
            return False
        elif self.root != item and self.rightChild is None and item > self.root:
            return False
        elif item == self.root:
            return True
        elif item < self.root:
            return self.leftChild.searchTreeSearch(item)
        else:
            return self.rightChild.searchTreeSearch(item)

    # Een methode die de BST doorloopt op zoek naar de knoop met de gegeven key. Indien het gevonden wordt geeft
    # de functie de BST met de key als root terug.
    #
    # return: De BST met het gegeven item als root, False indien het item niet in de boom aanwezig is.
    def retrieve(self, key):

        if not self.searchTreeSearch(key):
            return False
        elif key == self.root:
            return self
        elif key < self.root:
            return self.leftChild.retrieve(key)

        else:
            return self.rightChild.retrieve(key)

    # Een methode die de BST doorloopt op zoek naar het gegeven item. Indien het gevonden wordt geeft
    # de functie de BST met het item als root terug.
    #
    # return: De value van de node met gegeven id in de BST, False indien het item niet in de boom aanwezig is.
    def searchTreeRetrieve(self, key):

        if not self.searchTreeSearch(key):
            return (None, False)
        elif key == self.root:
            return (self.value, True)
        elif key < self.root:
            return self.leftChild.searchTreeRetrieve(key)

        else:
            return self.rightChild.searchTreeRetrieve(key)

    # Een methode die de BST inorder doorloopt en deze volgorde van zoeksleutels in een lijst teruggeeft.
    #
    # return: De functie returnt een lijst met de zoeksleutels van de BST in inorder volgorde terug.
    def inorderKeys(self, prt=None):
        lst = []

        if self.leftChild is None and self.rightChild is None:
            lst.append(self.root)

        elif self.leftChild is None and self.rightChild is not None:
            lst.append(self.root)
            lst += self.rightChild.inorderKeys()

        elif self.rightChild is None and self.leftChild is not None:
            lst += self.leftChild.inorderKeys()
            lst.append(self.root)
        else:
            lst += self.leftChild.inorderKeys()
            lst.append(self.root)
            lst += self.rightChild.inorderKeys()

        if prt == print:
            for e in lst:
                print(e)
        return lst

    # Een methode die de BST inorder doorloopt en deze volgorde van elementen in een lijst teruggeeft.
    #
    # return: De functie returnt een lijst met de elementen van de BST in inorder volgorde terug.
    def inorderTraverse(self, prt=None):
        lst = []

        if self.leftChild is None and self.rightChild is None:
            lst.append(self.value)

        elif self.leftChild is None and self.rightChild is not None:
            lst.append(self.value)
            lst += self.rightChild.inorderTraverse()

        elif self.rightChild is None and self.leftChild is not None:
            lst += self.leftChild.inorderTraverse()
            lst.append(self.value)
        else:
            lst += self.leftChild.inorderTraverse()
            lst.append(self.value)
            lst += self.rightChild.inorderTraverse()

        # if prt == print:
        #     for e in lst:
        #         print(e)

        if prt:
            for e in lst:
                prt(e)

        return lst

    # Een methode die gegeven item (TreeItem) insert op de correcte positie in de BST.
    def searchTreeInsert(self, item):

        inserted = False
        not_duplicate = True
        while not inserted:
            if self.root is None:
                self.root = item[0]
                self.value = item[1]
                inserted = True

            if item[0] == self.root and not inserted:
                inserted = True
                not_duplicate = False

            if self.leftChild is None and self.rightChild is None and not inserted:
                if item[0] < self.root:
                    self.leftChild = BST(self)
                    inserted = self.leftChild.searchTreeInsert(item)

                if item[0] > self.root:
                    self.rightChild = BST(self)
                    inserted = self.rightChild.searchTreeInsert(item)

            if self.leftChild is None and item[0] < self.root and not inserted:
                self.leftChild = BST(self)
                inserted = self.leftChild.searchTreeInsert(item)

            if self.rightChild is None and item[0] > self.root and not inserted:
                self.rightChild = BST(self)
                inserted = self.rightChild.searchTreeInsert(item)

            if item[0] < self.root and not inserted:
                not_duplicate = self.leftChild.searchTreeInsert(item)
                inserted = True

            if item[0] > self.root and not inserted:
                not_duplicate = self.rightChild.searchTreeInsert(item)
                inserted = True

        return inserted and not_duplicate

    # Een methode die voor een gegeven boom en id de inorder successor van het item met de gegeven id bepaalt.
    #
    # pre: De gegeven boom is een BST die het gegeven item bevat. De gegeven key is de zoeksleutel van
    # het item waarvan de inorder successor gezocht wordt.
    #
    # return: De inorder successor van het item met gegeven key in de gegeven BST als integer. False indien het
    # item geen inorder successor heeft.
    def inorder_succ(self, key):
        for i in range(len(self.inorderKeys())):
            if self.inorderKeys()[i] == key and i < len(self.inorderKeys()):
                return self.inorderKeys()[i + 1]
        return False

    # Een methode die het item met gegeven id dat aanwezig is in de BST swapped met zijn inorder successor.
    # En dit herhaald tot het gegeven item in een blad staat.
    #
    # pre: De boom bevat het gegeven item.
    # return: Het blad waarnaar de swap gebeurd is.
    def swap(self, key):
        inord = self.inorderKeys().copy()
        val = self.searchTreeRetrieve(key)

        lst = list()
        lst.append(self.retrieve(key))
        index = 0
        for i in range(len(inord)):
            if key == inord[i]:
                index = i

        for e in inord[index:]:
            if self.retrieve(e).leftChild is None and self.retrieve(e).rightChild is None:
                lst.append(self.retrieve(e))
                break
            else:
                lst.append(self.retrieve(e))

        for i in range(len(lst) - 1):
            lst[i].root = lst[i + 1].root
            lst[i].value = lst[i + 1].value
            lst[i + 1].root = key
            lst[i + 1].value = val

        return lst[-2]

    # Een methode die het item met gegeven id delete uit de BST.
    #
    # pre: het gegeven id is de zoeksleutel van het item dat verwijdert wordt
    #
    # return: True wordt teruggegeven als de delete succesvol was, anders wordt False gereturnd.
    def searchTreeDelete(self, key):
        if not self.searchTreeSearch(key):
            return False

        if self.retrieve(key).leftChild is None and self.retrieve(key).rightChild is None:
            if self.retrieve(key).parent.leftChild is not None and self.retrieve(key).parent.leftChild.root == key:
                self.retrieve(key).parent.leftChild = None
                return True
            else:
                self.retrieve(key).parent.rightChild = None
                return True

        parent = self.swap(key)
        if parent.leftChild is not None and parent.leftChild.root == key:
            parent.leftChild = None
            return True
        else:
            parent.rightChild = None
            return True

    # Een methode die de BST saved door een representatie van de BST op te stellen m.b.v.
    # dictionaries en lijsten. Deze representatie wordt als output teruggegeven.
    #
    # return: Een dictionary met een 'root' key die de wortel van de BST bevat en een 'children' key die
    # een lijst bevat met de representaties van de kinderen.
    def save(self):

        if self.rightChild is None and self.leftChild is None:
            return {'root': self.root}

        elif self.leftChild is None and self.rightChild is not None:

            return {'root': self.root,
                    'children': [None] + [self.rightChild.save()]}

        elif self.rightChild is None and self.leftChild is not None:

            return {'root': self.root,
                    'children': [self.leftChild.save()] + [None]}

        else:
            return {'root': self.root,
                    'children': [self.leftChild.save()] + [self.rightChild.save()]}

    # Een methode die een nieuwe BST inlaadt adv een respresentatie met dictionaries en lijsten.
    # post: self is herschreven en bevat de elementen vanuit de representatie.
    def load(self, dct):
        if dct is None:
            return None

        if len(dct) == 1:
            self.root = dct['root']
            self.value = dct['root']
            self.leftChild = None
            self.rightChild = None

            return self
        else:
            self.root = dct['root']
            self.value = dct['root']

            self.leftChild = BST(self)
            self.leftChild = self.leftChild.load(dct['children'][0])
            self.rightChild = BST(self)
            self.rightChild = self.rightChild.load(dct['children'][1])

            return self

class BSTTable(BST):

    def __init__(self):
        super().__init__()

    def tableIsEmpty(self):
        return self.isEmpty()

    def tableLength(self):
        return len(self.inorderTraverse())

    def tableInsert(self, key, item):
        return self.searchTreeInsert(createTreeItem(key, item))

    def tableDelete(self, key):
        return self.searchTreeDelete(key)

    def tableRetrieve(self,key):
        return self.searchTreeRetrieve(key)

    def tableSearch(self, key):
        return self.tableRetrieve(key)[0]

    def traverseTable(self, prt):
        return self.inorderTraverse(prt)



# Een functie die als parameters een lijst van integers l neemt. Vervolgens print de functie de lijst van getallen in
# een gesorteerde volgorde van klein naar groot met ieder element op een nieuwe lijn.
def BinarySort(l):
    tree = BST()
    for e in l:
        tree.searchTreeInsert(createTreeItem(e,e))
    return tree.inorderTraverse()


# Deze functie werdt overgenomen uit de gegeven code van een van de IP oefenzittingen en werdt lichtjes aangepast om
# te werken met het BST type.
def print_tree(tree, depth=0):
    """
    toon de boom maar gekanteld dus hij groeit van links naar rechts ipv van boven naar onder
    :param tree: de boom zelf
    :param depth: het niveau van de boom dat wordt afgedrukt (het indentatieniveau)
    :return: niets
    """
    if tree is None:
        print('%s' % ((depth * '\t') + '()'))
        return
    print('%s' % ((depth * '\t') + str(tree.root)))
    ## als kinderen
    print_tree(tree.leftChild, depth + 1)
    print_tree(tree.rightChild, depth + 1)


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