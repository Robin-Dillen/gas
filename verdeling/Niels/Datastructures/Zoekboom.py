def createTreeItem(key,val):
    return val;

class BST:
    def __init__(self,root = None,parent = None):
        self.root = root
        self.LeftTree = None
        self.RightTree = None
        self.parent = parent

    def load(self,tree):
        """
        Laadt een binaire zoekboom in
        :param tree: string vorm van boom met items
        :return: /
        preconditie:/

        postconditie:/
        """
        if(tree == None):
            self.root = None
        else: self.root = tree['root']
        self.LeftTree = None
        self.RightTree = None
        self.parent = None
        if(len(tree) == 2):
            if(tree['children'][0]!=None):
                self.LeftTree = BST()
                self.LeftTree.load(tree['children'][0])
                self.LeftTree.parent = self
            if (tree['children'][1] != None):
                self.RightTree = BST()
                self.RightTree.load(tree['children'][1])
                self.RightTree.parent = self
        return

    def searchTreeInsert(self,value):
        """
        voegt een item toe aan de boom
        :param value: waarde van het item
        :return: none
        precondition: None

        postcondition: None
        """
        if(self.root == None):
            self.root = value
        elif(self.LeftTree == None and value < self.root):
            nieuwe_knoop = BST(value)
            nieuwe_knoop.parent = self
            self.LeftTree = nieuwe_knoop
        elif (self.RightTree == None and value > self.root):
            nieuwe_knoop = BST(value)
            nieuwe_knoop.parent = self
            self.RightTree = nieuwe_knoop
        elif(self.LeftTree != None and value < self.root):
            self.LeftTree.searchTreeInsert(value)
        elif (self.RightTree != None and value > self.root):
            self.RightTree.searchTreeInsert(value)
        return True

    def zoekinordersuccessor(self,right = True):
        """
        Zoekt de inorder successor van een item
        :param right: Geeft aan of de recursieve functie al naar rechts is gesprongen of niet
        :return: De inorder succesor van een item
        precondition: het item mag geen blad zijn

        postcondition: None
        """
        if(right == False):
            if(self.LeftTree == None):
                return self
            else:
                return(self.LeftTree.zoekinordersuccessor(False))
        else:
            return(self.RightTree.zoekinordersuccessor(False))

    def searchTreeDelete(self,value):
        """
        verwijdert een item
        :param value: waarde van het item
        :return: none

        precondition: None

        postcondition: None
        """

        if(self.root == value):
            if(self.parent != None):
                if(self.LeftTree == None and self.RightTree == None):
                    if(self.parent.root < self.root):
                        self.parent.RightTree = None
                        self.root = None
                    elif(self.parent.root > self.root):
                        self.parent.LeftTree = None
                        self.root = None
                elif(self.LeftTree != None and self.RightTree != None):
                    inorder = self.zoekinordersuccessor()
                    inorder.parent.LeftTree = None
                    self.root = inorder.root
                    inorder.searchTreeDelete(inorder.root)
                    if (self.parent.root < self.root):
                        self.parent.RightTree = self.root
                    elif (self.parent.root > self.root):
                        self.parent.LeftTree = self.root
                elif (self.LeftTree != None and self.RightTree == None):
                    self.parent.LeftTree = self.LeftTree
                    self.root = None
                elif (self.LeftTree == None and self.RightTree != None):
                    self.parent.RightTree = self.RightTree
                    self.root = None
            elif(self.parent == None):
                if (self.LeftTree == None and self.RightTree == None):
                    self.root = None
                elif (self.LeftTree != None and self.RightTree != None):
                    inorder = self.zoekinordersuccessor()
                    if(self.RightTree.LeftTree == None):
                        inorder.parent.RightTree = None
                    else:
                        inorder.parent.LeftTree = None
                    self.root = inorder.root
                    inorder.searchTreeDelete(inorder.root)
                elif (self.LeftTree != None and self.RightTree == None):
                    self.LeftTree.parent = None
                    self.root = None
                elif (self.LeftTree == None and self.RightTree != None):
                    self.RightTree.parent = None
                    self.root = None
            return True
        elif(self.root < value and self.RightTree != None):
            self.RightTree.searchTreeDelete(value)
        elif (self.root > value and self.LeftTree != None):
            self.LeftTree.searchTreeDelete(value)
        return False

    def inorderTraverse(self,value):
        """
        Doorloopt een boom en print deze uit
        :param value: Geeft aan of het geprint moet worden of niet
        :return: True als het gelukt is

        precondition: None

        postcondition: None
        """
        if(value==print):
            if (self.LeftTree != None):
                self.LeftTree.inorderTraverse(print)
            print(self.root)
            if(self.RightTree!= None):
                self.RightTree.inorderTraverse(print)
            return True
        else: return False

    def getdepth(self, hoogte = 0):
        """
        geeft de diepte van de boom terug
        :return: diepte van de boom

        precondition: None

        postcondition: None
        """
        if(self.root == None):
            return hoogte
        elif(self.LeftTree == None and self.RightTree == None):
            return hoogte+1
        elif(self.LeftTree == None and self.RightTree != None):
            hoogte = self.RightTree.getdepth(hoogte)+1
        elif(self.LeftTree != None and self.RightTree == None):
            hoogte = self.LeftTree.getdepth(hoogte)+1
        elif(self.RightTree.getdepth() > self.LeftTree.getdepth()):
            hoogte = self.RightTree.getdepth(hoogte)+1
        elif(self.RightTree.getdepth() <= self.LeftTree.getdepth()):
            hoogte = self.LeftTree.getdepth(hoogte)+1
        return hoogte

    def getlength(self,lengte = 0):
        """
        geeft het aantal knopen van de boom terug
        :return: aantal knopen van de boom

        precondition: None

        postcondition: None
        """
        if(self.root == None):
            return lengte+1
        elif (self.LeftTree == None and self.RightTree == None):
            return lengte+1
        elif(self.LeftTree != None and self.RightTree == None):
            return lengte+self.LeftTree.getlength()+1
        elif(self.LeftTree == None and self.RightTree != None):
            return lengte+self.RightTree.getlength()+1
        return(self.LeftTree.getlength() + self.RightTree.getlength()+lengte+1)

    def isEmpty(self):
        """
        Kijkt na of een boom leeg is of niet
        :return: True als het leeg is, false als het niet leeg is
        precondition: None

        postcondition: None
        """
        if(self.root==None):
            return True;
        else:
            return False;

    def checkIfInTree(self,key):
        """
        Kijkt na of een gegeven item zich in de boom bevindt
        :param key: Item om na te kijken
        :return: True als het in de boom staat, false als dat niet zo is
        precondition: None

        postcondition: None
        """
        if(self.root == key):
            return True
        elif(self.root > key and self.LeftTree != None):
            return self.LeftTree.checkIfInTree(key)
        elif(self.root < key and self.RightTree != None):
            return self.RightTree.checkIfInTree(key)
        else: return False

    def searchTreeRetrieve(self,key):
        """
        Kijkt na of een gegeven item zich in de boom bevindt
        :param key: Item om na te kijken
        :return: (key,True) als het in de boom staat, (false,false) als dat niet zo is
        precondition: None

        postcondition: None
        """
        if(self.checkIfInTree(key)):
            return key,True
        else: return False,False

    def save(self):
        """
        slaat de boom correct op
        :return: dictionary van de boom

        precondition: None

        postcondition: None
        """
        if(self.LeftTree == None and self.RightTree == None):
            return {'root': self.root}
        elif(self.LeftTree != None and self.RightTree == None):
            return {'root': self.root, 'children':[self.LeftTree.save(),None]}
        elif(self.LeftTree == None and self.RightTree != None):
            return {'root': self.root, 'children':[None,self.RightTree.save()]}
        return {'root': self.root, 'children':[self.LeftTree.save(),self.RightTree.save()]}


class BSTTable:
    def __init__(self):
        self.a = BST()

    def load(self,tree):
        self.a.load(tree)

    def tableInsert(self,value):
        return self.a.searchTreeInsert(value)

    def tableDelete(self,value):
        return self.a.searchTreeDelete(value)

    def traverseTable(self,value):
        return self.a.inorderTraverse(value)

    def tableIsEmpty(self):
        return self.a.isEmpty()

    def tableRetrieve(self,value):
        return self.a.searchTreeRetrieve(value)

    def save(self):
        return self.a.save()

