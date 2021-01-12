class LinkedChain:
    def __init__(self):
        self.list = [None]

    def load(self, list):
        """
        Laadt een ketting in
        :param list: lijst van items
        :return: true als het gelukt is

        precondition: None

        postcondition: None
        """
        self.list = [None]
        for i in list:
            self.list.append(i)
        return True

    def add(self, value):
        """
        voegt een item toe op het einde van de ketting
        :param value: waarde van het item
        :return: none

        precondition: None

        postcondition: None
        """
        self.list.append(value)

    def insert(self,value):
        """
        voegt een item toe op positie index
        :param value: waarde van het item
        :return: True

        precondition: None

        postcondition: None
        """
        self.list.append(value)
        return True


    def delete(self, index):
        """
        verwijdert een item uit de ketting
        :param index: plaats waar het item moet worden verwijderd
        :return: True als succes

        precondition: de gegeven index/value moet bestaan in de ketting

        postcondition: lengte van de ketting zal verkleinen met 1
        """
        if (index > 0 and index < self.getLength()):
            self.list.pop(index)
            return True
        else:
            return False

    def print(self):
        """
        print de ketting af
        :return: none

        precondition: None

        postcondition: None
        """
        l = []
        for i in self.list:
            print(l)

    def getLength(self):
        """
        geeft de lengte van de ketting
        :return: lengte van de ketting

        precondition: None

        postcondition: None
        """
        return len(self.list) - 1

    def get_next_item(self, index):
        """
        geeft de lengte van het volgende item weer
        :param index: index van het opgegeven item
        :return: none

        precondition: lengte van de Ketting moet groter zijn dan 0

        postcondition: None
        """
        if (index == self.getLength()):
            return self.list[0]
        else:
            return self.list[index + 1]

    def get_previous_item(self, index):
        """
        geeft de lengte van het vorige item weer
        :param index: index van het opgegeven item
        :return: none

        precondition: lengte van de Ketting moet groter zijn dan 0

        postcondition: None
        """
        if (index == 0):
            return self.list[-1]
        else:
            return self.list[index - 1]

    def isEmpty(self):
        """
        Kijkt na of een ketting leeg is
        :return: True als het leeg is, false als het niet leeg is

        precondition: None

        postcondition: None
        """
        if (self.getLength() == 0):
            return True
        else:
            return False

    def retrieve(self, id):
        """
        Geeft een item terug op de gevraagde id
        :param id: id van het gevraagde item
        :return: Item als de id geldig is, none als dat niet zo is
        precondition: None

        postcondition: None
        """
        if(self.isEmpty()):
            return None, False
        for i in range(1, self.getLength()+1):
            if(self.list[i].getId() == id):
                return self.list[i], True
        return None, False

    def retrieveIndex(self, index):
        """
        Geeft een item terug op de gevraagde index
        :param index: index van het gevraagde item
        :return: Item, true als de index geldig is, none, False als dat niet zo is
        precondition: None

        postcondition: None
        """
        if(1<=index<=self.getLength()+1):
            return self.list[index], True
        return None, False


    def traverse(self,prnt):
        """
        Doorloopt de linkedchain
        :param prnt: geeft aan dat er geprint moet worden
        :return: True als het is gelukt
        """
        for i in range(1, self.getLength()+1):
            prnt(self.retrieveIndex(i)[0])
        return True

    def save(self):
        """
        slaat een ketting op
        :return: lijst met alle items van een ketting

        precondition: None

        postcondition: None
        """
        l = []
        for i in range(1, self.getLength()+1):
            l.append(self.list[i])
        return l


class LinkedChainTable:
    def __init__(self):
        self.a = LinkedChain()

    def load(self, tree):
        self.a.load(tree)

    def tableInsert(self,value):
        return self.a.insert(value)

    def tableDelete(self, value):
        return self.a.delete(value)

    def tableLength(self):
        return self.a.getLength()

    def tableIsEmpty(self):
        return self.a.isEmpty()

    def tableRetrieve(self, index):
        return self.a.retrieve(index)

    def traverseTable(self, prnt):
        return self.a.traverse(prnt)

    def save(self):
        return self.a.save()

if __name__ == "__main__":
    l = LinkedChain()
    print(l.isEmpty())
    print(l.getLength())
    print(l.retrieve(4)[1])
    print(l.insert(4, 500))
    print(l.isEmpty())
    print(l.insert(1, 500))
    print(l.retrieve(1)[0])
    print(l.retrieve(1)[1])
    print(l.save())
    print(l.insert(1, 600))
    print(l.getLength())
    print(l.save())
    l.load([10, -9, 15])
    l.insert(3, 20)
    print(l.delete(0))
    print(l.save())
    print(l.delete(1))
    print(l.save())

    l = LinkedChainTable()
    print(l.tableIsEmpty())
    print(l.tableLength())
    print(l.tableRetrieve(4)[1])
    print(l.tableInsert(4, 500))
    print(l.tableIsEmpty())
    print(l.tableInsert(1, 500))
    print(l.tableRetrieve(1)[0])
    print(l.tableRetrieve(1)[1])
    print(l.save())
    print(l.tableInsert(1, 600))
    print(l.save())
    l.load([10, -9, 15])
    l.tableInsert(3, 20)
    print(l.tableDelete(0))
    print(l.save())
    print(l.tableDelete(10))
    print(l.save())