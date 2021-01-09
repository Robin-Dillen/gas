def createTreeItem(key,val):
    """
    Maakt een TreeItem op maat van de implementatie van de klasse.
    :param key: Waarde van het item
    :param val: Waarde van het item
    :return: Waarde van het item
    """
    return val

class TwoThreeTree:
    def __init__(self):
        self.root = None
        self.LeftTree = None
        self.MiddleTree = None
        self.RightTree = None
        self.parent = None
        pass

    def load(self,tree):
        """
        Laadt een 2-3 boom in
        :param tree: vector van de boom
        :return: True als het gelukt is, false als het niet gelukt is.
        preconditie: /

        postconditie: De nieuwe boom is ingeladen
        """
        if(tree == None):
            self.root = None
        else:
            self.root = tree['root']
        self.LeftTree = None
        self.RightTree = None
        self.MiddleTree = None
        self.parent = None

        if (len(tree) == 2):
            if(len(self.root) == 1):
                self.LeftTree = TwoThreeTree()
                self.LeftTree.load(tree['children'][0])
                self.LeftTree.parent = self
                self.RightTree = TwoThreeTree()
                self.RightTree.load(tree['children'][1])
                self.RightTree.parent = self
            elif(len(self.root) == 2):
                self.LeftTree = TwoThreeTree()
                self.LeftTree.load(tree['children'][0])
                self.LeftTree.parent = self
                self.MiddleTree = TwoThreeTree()
                self.MiddleTree.load(tree['children'][1])
                self.MiddleTree.parent = self
                self.RightTree = TwoThreeTree()
                self.RightTree.load(tree['children'][2])
                self.RightTree.parent = self
        return True

    def pushUp(self,subtree):
        """
        Volgt een algoritme om een item omhoog te pushen in een 2-3 boom.
        :param subtree: Subtree is een parameter die weergeeft of de knoop het linkse, middelste of rechtse kind is van zijn ouder.
        :return: /
        preconditie: /

        postconditie: /
        """
        if(self.parent == None):
            left_node = TwoThreeTree()
            left_node.root = [self.root[0]]
            left_node.parent = self
            right_node = TwoThreeTree()
            right_node.root = [self.root[2]]
            right_node.parent = self
            self.root = [self.root[1]]

            if(subtree == "Left"):
                left_node.LeftTree = self.LeftTree
                self.LeftTree.parent = left_node
                new_right_node = TwoThreeTree()
                left_node.RightTree = new_right_node
                new_right_node.parent = left_node
                new_right_node.root = [self.LeftTree.root[1]]
                self.LeftTree.root = [self.LeftTree.root[0]]
                right_node.LeftTree = self.MiddleTree
                self.MiddleTree.parent = right_node
                right_node.RightTree = self.RightTree
                self.RightTree.parent = right_node
            elif(subtree == "Right"):
                right_node.RightTree = self.RightTree
                self.RightTree.parent = right_node
                new_left_node = TwoThreeTree()
                right_node.LeftTree = new_left_node
                new_left_node.parent = right_node
                new_left_node.root = [self.RightTree.root[0]]
                self.RightTree.root = [self.RightTree.root[1]]
                left_node.RightTree = self.MiddleTree
                self.MiddleTree.parent = left_node
                left_node.LeftTree = self.LeftTree
                self.LeftTree.parent = left_node
            elif(subtree == "Middle"):
                left_node.LeftTree = self.LeftTree
                self.LeftTree.parent = left_node
                new_right_node = TwoThreeTree()
                new_right_node.parent = left_node
                left_node.RightTree = new_right_node
                new_right_node.root = [self.MiddleTree.root[0]]
                new_left_node = TwoThreeTree()
                new_left_node.parent = right_node
                right_node.LeftTree = new_left_node
                new_left_node.root = [self.MiddleTree.root[1]]
                right_node.RightTree = self.RightTree

            self.MiddleTree = None
            self.LeftTree = left_node
            self.RightTree = right_node

        elif(len(self.parent.root) == 1):
            middle_node = TwoThreeTree()
            middle_node.parent = self.parent
            self.parent.MiddleTree = middle_node
            if(self.root[0]<self.parent.root[0]):
                middle_node.root = [self.root[2]]
                self.parent.root.insert(0,self.root[1])
                self.root = [self.root[0]]
            else:
                middle_node.root = [self.root[0]]
                self.parent.root.insert(1,self.root[1])
                self.root = [self.root[2]]
        elif(len(self.parent.root) == 2):
            if(self.root[0]<self.parent.root[0]):
                self.parent.root.insert(0,self.root[1])
                self.root = [self.root[0],self.root[2]]
                self.parent.pushUp("Left")
            elif(self.root[0]>self.parent.root[1]):
                self.parent.root.insert(2, self.root[1])
                self.root = [self.root[0],self.root[2]]
                self.parent.pushUp("Right")
            else:
                self.parent.root.insert(1, self.root[1])
                self.root = [self.root[0],self.root[2]]
                self.parent.pushUp("Middle")

    def insertItem(self,value):
        """
        Voegt een item toe aan de 2-3 boom
        :param value: waarde van item dat wordt toegevoegd
        :return: /

        preconditie: de boom mag geen item bevatten met waarde "value"

        postconditie: lengte van de 2-3 boom moet vergoten met 1
        """
        if(self.root == None):
            self.root = [value]
        elif(len(self.root) == 1):
            if(self.LeftTree == None and self.RightTree == None):
                if(value<self.root[0]):
                    self.root.insert(0,value)
                else:
                    self.root.insert(1, value)
            elif(value<self.root[0]):
                self.LeftTree.insertItem(value)
            elif(value>self.root[0]):
                self.RightTree.insertItem(value)
        elif(len(self.root) == 2):
            if(self.LeftTree == None and self.MiddleTree == None and self.RightTree == None):
                if(value<self.root[0]):
                    self.root.insert(0,value)
                elif(value>self.root[0] and value<self.root[1]):
                    self.root.insert(1, value)
                else:
                    self.root.append(value)
                self.pushUp()
            else:
                if(value<self.root[0]):
                    self.LeftTree.insertItem(value)
                elif(value>self.root[1]):
                    self.RightTree.insertItem(value)
                else:
                    self.MiddleTree.insertItem(value)
        return True

    def zoekinordersuccessor(self,right = True, node = 1):
        """
        Zoekt de inorder successor van een gegeven item in een 2-3 boom.
        :param right: Geeft weer of er al naar rechts in gejumped of niet.
        :param node: Kijkt na of het een 2 knoop of 3 knoop is.
        :return: de inorder successor
        preconditie: Item mag geen blad zijn

        postconditie: /
        """
        if(right == False):
            if(len(self.root) == 1):
                if (self.LeftTree == None):
                    return self
                else:
                    return (self.LeftTree.zoekinordersuccessor(False))
            elif (len(self.root) == 2):
                if(node == 1):
                    if (self.LeftTree == None):
                        return self
                    else:
                        return (self.LeftTree.zoekinordersuccessor(False))
                if(node == 2):
                    if (self.MiddleTree == None):
                        return self
                    else:
                        return (self.MiddleTree.zoekinordersuccessor(False))
        else:
            if(len(self.root) == 1):
                return(self.RightTree.zoekinordersuccessor(False))
            elif(len(self.root) == 2):
                if(node == 1):
                    return(self.MiddleTree.zoekinordersuccessor(False))
                elif(node == 2):
                    return (self.RightTree.zoekinordersuccessor(False))

    def makebalanced(self):
        """
        Maakt een 2-3 boom balanced na het verwijderen van een item.
        :return: None
        preconditie: Item moet een blad zijn

        postconditie: Boom is balanced
        """
        if(self.parent == None):
            return
        else:
            if(self.root<self.parent.root):
                self.parent.root[1] = self.parent.RightTree.root[0]
                self.parent.MiddleTree = self.parent.RightTree.LeftTree
                self.parent.RightTree = self.parent.RightTree.RightTree
            elif(self.root>self.parent.root):
                self.parent.root = [self.parent.LeftTree.root[0],self.parent.root[0]]
                self.parent.MiddleTree = self.parent.LeftTree.RightTree
                self.parent.RightTree = self.parent.LeftTree.Lefttree
        return

    def zetinblad(self, node = 1):
        """
        Verplaatst een item die verwijdert moet worden naar een blad met behulp van de inorder successor.
        :param node: Kijkt na of het item het linkse item is in de knoop of het rechtse item is in de knoop.
        :return: Het item dat is geswitched met het te verwijderen item.
        preconditie: /

        postconditie: /
        """
        inorder = self.zoekinordersuccessor(node)
        value = inorder.root[0]
        inorder.root[0] = self.root[node-1]
        self.root[node - 1] = value
        return inorder

    def deleteItem(self,value):
        """
        Verwijdert een item uit de 2-3 boom.
        :param value: waarde van item dat wordt toegevoegd
        :return: /

        preconditie: de boom moet een item bevatten met waarde "value"

        postconditie: lengte van de 2-3 boom moet verkleinen met 1
        """
        #2-knoop
        if(len(self.root) == 1):
            #juiste waarde
            if(value == self.root[0]):
                #geen kinderen
                if(self.LeftTree == None):
                    #lengte van ouder is 0
                    if(self.parent == None):
                        self.root = None
                    #lengte van ouder is 1
                    elif(len(self.parent.root) == 1):
                        #links kind
                        if (self.root[0] < self.parent.root[0]):
                            #rechtse sibling 2?
                            if(len(self.parent.RightTree) == 2):
                                self.root = [self.parent.root[0]]
                                self.parent.root = [self.parent.RightTree.root[0]]
                                self.parent.RightTree.root = [self.parent.RightTree.root[1]]
                            #linkse sibling 2?
                            elif(self.parent.parent != None):
                                if(len(self.parent.parent) == 1):
                                    if(self.parent.root[0]>self.parent.parent.root[0]):
                                        if(len(self.parent.parent.LeftTree.RightTree) == 2):
                                            self.root = [self.parent.parent.root[0]]
                                            self.parent.parent.root = [self.parent.parent.LeftTree.RightTree.root[1]]
                                            self.parent.parent.LeftTree.RightTree.root = [self.parent.parent.LeftTree.RightTree.root[0]]
                                            return True
                                elif(len(self.parent.parent) == 2):
                                    if(self.parent.root[0]>self.parent.parent.root[0] and self.parent.root[0]<self.parent.parent.root[1]):
                                        if(len(self.parent.parent.LeftTree.RightTree) == 2):
                                            self.root = [self.parent.parent.root]
                                            self.parent.parent.root = [self.parent.parent.LeftTree.RightTree.root[1],self.parent.parent.root[1]]
                                            self.parent.parent.LeftTree.RightTree.root = [self.parent.parent.LeftTree.RightTree.root[0]]
                                            return True
                                    elif(self.parent.root[0]>self.parent.parent.root[1]):
                                        if(len(self.parent.parent.MiddleTree.RightTree) == 2):
                                            self.root = [self.parent.parent.root]
                                            self.parent.parent.root = [self.parent.parent.root[0],self.parent.parent.MiddleTree.RightTree.root[1]]
                                            self.parent.parent.MiddleTree.RightTree.root = [self.parent.parent.MiddleTree.RightTree.root[0]]
                                            return True
                            #geen sibling met 2 items
                            else:
                                self.parent.LeftTree = None
                                self.parent.root = [self.parent.root[0],self.parent.RightTree.root[0]]
                                self.parent.RightTree = None
                                self.makebalanced()
                                return True
                        #rechts kind
                        elif(self.root[0] > self.parent.root[1]):
                            # linkse sibling 2?
                            if (len(self.parent.LeftTree) == 2):
                                self.root = [self.parent.root[0]]
                                self.parent.root = [self.parent.LeftTree.root[1]]
                                self.parent.LeftTree.root = [self.parent.LeftTree.root[0]]
                                return True
                            # Rechtse sibling 2?
                            elif (self.parent.parent != None):
                                if (len(self.parent.parent) == 1):
                                    if (self.parent.root[0] < self.parent.parent.root[0]):
                                        if (len(self.parent.parent.RightTree.LeftTree) == 2):
                                            self.root = [self.parent.parent.root[0]]
                                            self.parent.parent.root = [self.parent.parent.RightTree.LeftTree.root[0]]
                                            self.parent.parent.RightTree.LeftTree.root = [self.parent.parent.RightTree.LeftTree.root[1]]
                                            return True
                                elif (len(self.parent.parent) == 2):
                                    if (self.parent.root[0] > self.parent.parent.root[0] and self.parent.root[0] <self.parent.parent.root[1]):
                                        if (len(self.parent.parent.RightTree.LeftTree) == 2):
                                            self.root = [self.parent.parent.root]
                                            self.parent.parent.root = [self.parent.parent.root[0],self.parent.parent.RightTree.LeftTree.root[0]]
                                            self.parent.parent.RightTree.LeftTree.root = [self.parent.parent.RightTree.LeftTree.root[1]]
                                            return True
                                    elif (self.parent.root[0] < self.parent.parent.root[0]):
                                        if (len(self.parent.parent.MiddleTree.LeftTree) == 2):
                                            self.root = [self.parent.parent.root]
                                            self.parent.parent.root = [self.parent.parent.MiddleTree.LeftTree.root[0],self.parent.parent.root[1]]
                                            self.parent.parent.MiddleTree.LeftTree.root = [self.parent.parent.MiddleTree.LeftTree.root[1]]
                                            return True
                            # geen sibling met 2 items
                            else:
                                self.parent.RightTree = None
                                self.parent.root.insert(1, self.parent.LeftTree.root[0])
                                self.parent.LeftTree = None
                                self.makebalanced()
                                return True
                    # lengte van ouder is 2
                    elif(len(self.parent.root) == 2):
                        #linksekind
                        if(self.root[0]<self.parent.root[0]):
                            # rechtse sibling 2?
                            if (len(self.parent.MiddleTree) == 2):
                                self.root = [self.parent.root[0]]
                                self.parent.root = [self.parent.MiddleTree.root[0],self.parent.root[1]]
                                self.parent.MiddleTree.root = [self.parent.MiddleTree.root[1]]
                                return True
                            # linkse sibling 2?
                            elif (self.parent.parent != None):
                                if (len(self.parent.parent) == 1):
                                    if (self.parent.root[0] > self.parent.parent.root[0]):
                                        if (len(self.parent.parent.LeftTree.RightTree) == 2):
                                            self.root = [self.parent.parent.root[0]]
                                            self.parent.parent.root = [self.parent.parent.LeftTree.RightTree.root[1]]
                                            self.parent.parent.LeftTree.RightTree.root = [self.parent.parent.LeftTree.RightTree.root[0]]
                                            return True
                                elif (len(self.parent.parent) == 2):
                                    if (self.parent.root[0] > self.parent.parent.root[0] and self.parent.root[0] <self.parent.parent.root[1]):
                                        if (len(self.parent.parent.LeftTree.RightTree) == 2):
                                            self.root = [self.parent.parent.root]
                                            self.parent.parent.root = [self.parent.parent.LeftTree.RightTree.root[1],self.parent.parent.root[1]]
                                            self.parent.parent.LeftTree.RightTree.root = [self.parent.parent.LeftTree.RightTree.root[0]]
                                            return True
                                    elif (self.parent.root[0] > self.parent.parent.root[1]):
                                        if (len(self.parent.parent.MiddleTree.RightTree) == 2):
                                            self.root = [self.parent.parent.root]
                                            self.parent.parent.root = [self.parent.parent.root[0],self.parent.parent.MiddleTree.RightTree.root[1]]
                                            self.parent.parent.MiddleTree.RightTree.root = [self.parent.parent.MiddleTree.RightTree.root[0]]
                                            return True
                            # geen sibling met 2 items
                            else:
                                self.root = [self.parent.root[0],self.parent.MiddleTree.root[0]]
                                self.parent.root = [self.parent.root[1]]
                                self.parent.MiddleTree = None
                                return True
                        # middelste kind
                        elif(self.root[0]>self.parent.root[0] and self.root[0]<self.parent.root[1]):
                            # linkse sibling 2?
                            if(len(self.parent.LeftTree.root) == 2):
                                self.root = [self.parent.root[0]]
                                self.parent.root = [self.parent.LeftTree.root[1],self.parent.root[1]]
                                self.parent.LeftTree.root = [self.parent.LeftTree.root[0]]
                                return True
                            # rechtse sibling 2?
                            elif(len(self.parent.RightTree.root) == 2):
                                self.root = [self.parent.root[1]]
                                self.parent.root = [self.parent.root[0], self.parent.RightTree.root[0]]
                                self.parent.RightTree.root = [self.parent.RightTree.root[1]]
                                return True
                            #geen sibling met 2 items
                            else:
                                self.parent.MiddleTree = None
                                self.parent.LeftTree.root = [self.parent.LeftTree.root[0],self.parent.root[0]]
                                self.parent.root = [self.parent.root[1]]
                                return True
                        # Rechtsekind
                        elif(self.root[0]>self.parent.root[1]):
                            # linkse sibling 2?
                            if(len(self.parent.MiddleTree.root) == 2):
                                self.root = [self.parent.root[1]]
                                self.parent.root = [self.parent.root[0], self.parent.MiddleTree.root[1]]
                                self.parent.MiddleTree.root = [self.parent.MiddleTree.root[0]]
                                return True
                            # rechtse sibling 2?
                            elif (self.parent.parent != None):
                                if (len(self.parent.parent) == 1):
                                    if (self.parent.root[0] < self.parent.parent.root[0]):
                                        if (len(self.parent.parent.RightTree.LeftTree) == 2):
                                            self.root = [self.parent.parent.root[0]]
                                            self.parent.parent.root = [self.parent.parent.RightTree.LeftTree.root[0]]
                                            self.parent.parent.RightTree.LeftTree.root = [self.parent.parent.RightTree.LeftTree.root[1]]
                                            return True
                                elif (len(self.parent.parent) == 2):
                                    if (self.parent.root[0] > self.parent.parent.root[0] and self.parent.root[0] <self.parent.parent.root[1]):
                                        if (len(self.parent.parent.RightTree.LeftTree) == 2):
                                            self.root = [self.parent.parent.root]
                                            self.parent.parent.root = [self.parent.parent.root[0],self.parent.parent.RightTree.LeftTree.root[0]]
                                            self.parent.parent.RightTree.LeftTree.root = [self.parent.parent.RightTree.LeftTree.root[1]]
                                            return True
                                    elif (self.parent.root[0] < self.parent.parent.root[0]):
                                        if (len(self.parent.parent.MiddleTree.LeftTree) == 2):
                                            self.root = [self.parent.parent.root]
                                            self.parent.parent.root = [self.parent.parent.MiddleTree.LeftTree.root[0],self.parent.parent.root[1]]
                                            self.parent.parent.MiddleTree.LeftTree.root = [self.parent.parent.MiddleTree.LeftTree.root[1]]
                                            return True
                            #geen sibling met 2 items
                            else:
                                self.root = [self.parent.MiddleTree.root[0],self.parent.root[1]]
                                self.parent.root = [self.parent.root[0]]
                                self.parent.MiddleTree = None
                                return True
                #kinderen
                else:
                    inorder = self.zetinblad(1)
                    return inorder.deleteItem(value)
            elif(self.LeftTree != None):
                if(value<self.root[0]):
                    return self.LeftTree.deleteItem(value)
                elif(value>self.root[0]):
                    return self.RightTree.deleteItem(value)
            return False
        #3-knoop
        elif(len(self.root) == 2):
            if(value == self.root[0]):
                if(self.LeftTree == None):
                    self.root = [self.root[1]]
                    return True
                else:
                    inorder = self.zetinblad(1)
                    return inorder.deleteItem(value)
            elif(value == self.root[1]):
                if(self.LeftTree == None):
                    self.root = [self.root[0]]
                    return True
                else:
                    inorder = self.zetinblad(2)
                    return inorder.deleteItem(value)
            elif(self.LeftTree != None):
                if(value<self.root[0]):
                    return self.LeftTree.deleteItem(value)
                elif(value>self.root[0] and value<self.root[1]):
                     return self.MiddleTree.deleteItem(value)
                elif(value>self.root[1]):
                    return self.RightTree.deleteItem(value)
            return False
        else:
            return False

    def inorderTraverse(self, value = None):
        """
        Doorloopt een 2-3 boom en print het uit
        :return: /

        preconditie: /

        postconditie: /
        """
        if(value==print):
            if (self.LeftTree != None):
                self.LeftTree.inorderTraverse(print)
            print(self.root[0])
            if(self.MiddleTree!= None):
                self.MiddleTree.inorderTraverse(print)
            if(len(self.root)==2):
                print(self.root[1])
            if (self.RightTree != None):
                self.RightTree.inorderTraverse(print)
            return True
        else: return False

    def isEmpty(self):
        """
        Kijkt na of de boom leeg is
        :return: True als het leeg is, false als het niet leeg is

        preconditie: /

        postconditie: /
        """
        if(self.root == None):
            return True
        else: return False

    def checkIfInTree(self,key):
        """
        Kijkt na of een gegeven item zich in een 2-3 boom bevindt.
        :param key: het gegeven item
        :return: True als het zich in de boom bevindt, False als dat niet het geval is.
        preconditie: /

        postconditie: /
        """
        if(len(self.root) == 1):
            if (self.root == key):
                return True
            elif (self.root > key and self.LeftTree != None):
                return self.LeftTree.checkIfInTree(key)
            elif (self.root < key and self.RightTree != None):
                return self.RightTree.checkIfInTree(key)
            else:
                return False
        elif(len(self.root) == 2):
            if (self.root[0] == key):
                return True
            elif(self.root[1] == key):
                return True
            elif(key < self.root[0] and self.LeftTree != None):
                return self.LeftTree.checkIfInTree(key)
            elif(key > self.root[0] and key < self.root[1] and self.MiddleTree != None):
                return self.MiddleTree.checkIfInTree(key)
            elif(key > self.root[1] and self.RightTree != None):
                return self.RightTree.checkIfInTree(key)
            else:
                return False
        return False

    def retrieveItem(self,key):
        """
        Zoekt een item op in de 2-3 boom
        :return: True als het item gevonden is, false als het item niet gevonden is

        preconditie: /

        postconditie: /
        """
        if (self.checkIfInTree(key)):
            return [key, True]
        else:
            return [False, False]

    def save(self):
        """
        slaat een 2-3 boom correct op
        :return: dictionary met alle knopen van de 2-3 boom

        preconditie: /

        postconditie: /
        """
        if (len(self.root) == 1):
            if (self.LeftTree == None):
                return {'root': [self.root[0]]}
            else:
                return {'root': [self.root[0]], 'children': [self.LeftTree.save(), self.RightTree.save()]}
        elif (len(self.root) == 2):
            if (self.LeftTree == None):
                return {'root': self.root}
            else:
                return {'root': [self.root],'children': [self.LeftTree.save(), self.MiddleTree.save(), self.RightTree.save()]}


class TwoThreeTreeTable:
    def __init__(self):
        self.a = TwoThreeTree()

    def load(self,value):
        return self.a.load(value)

    def traverseTable(self,value):
        return self.a.inorderTraverse(value)

    def tableIsEmpty(self):
        return self.a.isEmpty()

    def tableRetrieve(self,value):
        return self.a.retrieveItem(value)

    def tableInsert(self,value):
        return self.a.insertItem(value)

    def tableDelete(self,value):
        return self.a.deleteItem(value)

    def tableLength(self):
        return self.a.getLength()

    def save(self):
        return self.a.save()

t = TwoThreeTreeTable()
print(t.tableIsEmpty())
print(t.tableInsert(createTreeItem(8,8)))
print(t.tableInsert(createTreeItem(5,5)))
print(t.tableIsEmpty())
print(t.tableRetrieve(5)[0])
print(t.tableRetrieve(5)[1])
t.traverseTable(print)
print(t.save())
t.load({'root': [10],'children':[{'root':[5]},{'root':[11]}]})
t.tableInsert(createTreeItem(15,15))
print(t.tableDelete(0))
print(t.save())
print(t.tableDelete(10))
print(t.save())