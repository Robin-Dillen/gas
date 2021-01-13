from verdeling.Khemin.Datastructures.LinkedChain import *


def createTableItem(key,val):
    return key, val


class Hashmap:
    """
    Om de implementatie van separate chaining aan te passen hoeft er enkel in __init__ en load een aanpassing gebeuren
    op voorwaarde dat de nieuwe implementatie beschikt over een wrapper met dezelfde benamingen als LinkedChainTable().
    """
    def __init__(self, type, n):
        """
        Initialiseert een nieuwe hashmap met gegeven grootte n. Type geeft
        """
        self.type = type
        if type == "sep":
            self.items = [LinkedChainTable()]*n   # regel waar implementatie van seperate chaining kan verandert worden
        else:
            self.items = [None]*n
        self.n = n

    def hash(self, searchkey):
        """
        De hashfunctie van de Hashmap die gebruikt wordt bij het berekenen van het adres.
        :param searchkey: De zoeksleutel waarvoor een adres berekent wordt.
        :return: Een integer die het adres geeft voor het item met de gegeven zoeksleutel.
        """
        return searchkey % self.n

    def isEmpty(self):
        """
        Geeft terug of de Hashmap leeg is of niet.
        :return: True als de Hashmap leeg is, anders False.
        """
        if self.type == "sep":
            for e in self.items:
                if e.tableIsEmpty():
                    return False
        else:
            for e in self.items:
                if e is not None:
                    return False

        return True

    def isFull(self):
        """
        Geeft terug of de Hashmap vol zit of niet. Dit kan enkel bij linear of quadratic probing.
        :return: True als de Hashmap vol zit, anders False.
        """
        if self.type == "sep":
            for e in self.items:
                if e.tableIsEmpty():
                    return False
        else:
            if None in self.items:
                return False

        return True

    def getLength(self):
        """
        Geeft de grootte van de Hashmap terug.

        :return: De grootte van de Hashmap(integer).
        """
        return self.n

    def traverse(self, prt):
        """
        Geeft de lijst van elementen terug.

        :param prt: Optionele parameter die weergeeft of de traverse geprint moet worden.
        :return: Een lijst die de elementen van de Hashmap bevat (integers voor "lin" en "quad" en LinkedChain voor "sep".
        """
        lst = []
        for e in self.items:
            if(e is not None):
                prt(e[1])
                lst.append(e[1])
        return lst

    def insert(self, item):
        """
        Voegt het gegeven item toe in de Hashmap.
        :param item: Het item dat toegevoegd wordt in de Hashmap.
        :return: True als insert gelukt is, anders False.
        """
        if self.type == "lin":
            index = self.hash(item[0])
            if self.items[index] is None:
                self.items[index] = item
                return True
            else:
                i = (index + 1) % self.n
                while i != index:
                    if self.items[i] is None:
                        self.items[i] = item
                        return True
                    i = (i + 1) % self.n
                return False

        if self.type == "quad":
            index = self.hash(item[0])
            if self.items[index] is None:
                self.items[index] = item
                return True
            else:
                j = 1
                i = (index + j**2) % self.n
                while i != index:
                    if self.items[i] is None:
                        self.items[i] = item
                        return True
                    j += 1
                    i = (i + j**2) % self.n
                return False

        if self.type == "sep":
            index = self.hash(item[0])
            self.items[index].tableInsert(1, item)
            return True

    def retrieve(self, searchkey):
        """
        Haalt het item met gegeven searchkey op uit de Hashmap.
        :param searchkey: De zoeksleutel van het item dat opgehaald wordt.
        :return: (TableItem,True) als de retrieve succesvol is, anders (None, False)
        """
        if self.type == "lin":
            index = self.hash(searchkey)
            if self.items[index] is None:
                return None, False
            if self.items[index][0] == searchkey:
                return self.items[index][1], True
            else:
                i = (index + 1) % self.n
                while i != index:
                    if self.items[i][0] == searchkey:
                        return self.items[i][1], True
                    i = (i + 1) % self.n
                return None, False

        if self.type == "quad":
            index = self.hash(searchkey)
            if self.items[index] is None:
                return None, False
            if self.items[index][0] == searchkey:
                return self.items[index][1], True
            else:
                j = 1
                i = (index + j ** 2) % self.n
                while i != index:
                    if self.items[i][0] == searchkey:
                        return self.items[i][1], True
                    j += 1
                    i = (i + j ** 2) % self.n
                return None, False

        if self.type == "sep":
            index = self.hash(searchkey)
            if self.items[index] is None:
                return None, False
            if self.items[index].tableIsEmpty():
                return None, False
            else:
                for i in range(1, self.items[index].tableLength()+1):
                    if self.items[index].tableRetrieve(i)[0] == searchkey:
                        return self.items[index].tableRetrieve(i)[1], True
                return None, False

    def delete(self, searchkey):
        """
        Verwijdert het item met gegeven searchkey uit de Hashmap.

        :param searchkey: De zoeksleutel van het item dat gedelete wordt.
        :return: True als de delete succesvol is, anders False.
        """

        if self.type == "lin":
            index = self.hash(searchkey)
            if self.items[index] is None:
                return False

            if self.items[index][0] == searchkey:
                self.items[index] = None
                return True
            else:
                i = (index + 1) % self.n
                while i != index:
                    if self.items[i] is None:
                        return False

                    if self.items[i][0] == searchkey:
                        self.items[i] = None
                        return True
                    i = (i + 1) % self.n
                return False

        if self.type == "quad":
            index = self.hash(searchkey)
            if self.items[index] is None:
                return False

            if self.items[index][0] == searchkey:
                self.items[index] = None
                return True
            else:
                j = 1
                i = (index + j**2) % self.n
                while i != index:
                    if self.items[i] is None:
                        return False

                    if self.items[i][0] == searchkey:
                        self.items[i] = None
                        return True
                    j += 1
                    i = (i + j**2) % self.n
                return False

        if self.type == "sep":
            index = self.hash(searchkey)
            if self.items[index].tableIsEmpty():
                return False
            else:
                for i in range(1, self.items[index].getLength() + 1):
                    if self.items[index].tableRetrieve(i)[0][0] == searchkey:
                        self.items[index].tableDelete(i)
                        return True
                return False

    def save(self):
        """
        Saved de hashmap in een representatie mbv een dictionary met type en items als keys en de respectievelijke
        waardes als values. Value van type is een string. De items worden gerepresenteerd als een lijst van getallen
        met None op de open plaatsen (lin en quad) en een lijst van lijsten met None op de open plaatsen (sep)

        :return: De dictionary als representatie voor de gesavede hashmap.
        """
        dct = {
            "type" : "" ,
            "items" : list()
        }
        if self.type == "sep":
            dct["type"] = self.type
            for e in self.items:
                if e.tableIsEmpty():
                    dct["items"].append(None)
                else:
                    l = e.save()
                    for i in range(0, len(l)):
                        l[i] = l[i][1]
                    dct["items"].append(l)

        else:
            dct["type"] = self.type
            for e in self.items:
                if e is None:
                    dct["items"].append(e)
                else:
                    dct["items"].append(e[1])

        return dct

    def load(self, dct):
        """
        Laadt een niewue hashmap in vanuit de gegeven representaite voor een gesavede hashmap.
        :param dct: De dictionary die de gesavede hashmap voorstelt.
        :post: self is herschreven naar een hashmap met de inhoud vanuit de gegeven dictionary
        """
        self.items = list()
        if dct["type"] == "sep":
            self.type = dct["type"]
            for i in range(0, len(dct["items"])):
                if dct["items"][i] is None:
                    self.items.append(LinkedChainTable())
                else:
                    k = list()
                    for j in range(0, len(dct["items"][i])):
                        k.append(createTableItem(dct["items"][i][j], dct["items"][i][j]))
                    l = LinkedChainTable()
                    l.load(k)
                    self.items.append(l)
            self.n = len(dct["items"])

        else:
            self.type = dct["type"]
            for i in range(0, len(dct["items"])):
                if dct["items"][i] is None:
                    self.items.append(None)
                else:
                    self.items.append(createTableItem(dct["items"][i], dct["items"][i]))
            self.n = len(dct["items"])


class HashmapTable(Hashmap):
    def __init__(self, type, n):
        super().__init__(type,n)

    def tableIsEmpty(self):
        return self.isEmpty()

    def tableLength(self):
        return self.getLength()

    def tableInsert(self, item):
        return self.insert(createTableItem(item.getId(), item))

    def tableDelete(self, searchkey):
        return self.delete(searchkey)

    def tableRetrieve(self, searchkey):
        return self.retrieve(searchkey)

    def traverseTable(self, prt):
        return self.traverse(prt)



if __name__ == "__main__":
    t = Hashmap("lin", 3)
    print(t.isEmpty())
    print(t.tableInsert(createTableItem(8, 8)))
    print(t.tableInsert(createTableItem(5, 5)))
    print(t.tableInsert(createTableItem(10, 10)))
    print(t.tableInsert(createTableItem(15, 15)))
    print(t.isEmpty())
    print(t.tableRetrieve(5)[0])
    print(t.tableRetrieve(5)[1])
    print(t.save())
    t.load({'type': 'lin', 'items': [10, None, 2, 3, None]})
    t.tableInsert(createTableItem(15, 15))
    print(t.tableDelete(0))
    print(t.save())
    print(t.tableDelete(10))
    print(t.save())

    t.load({'type': 'quad', 'items': [10, None, 2, 3, None]})
    t.tableInsert(createTableItem(15, 15))
    print(t.tableDelete(0))
    print(t.save())
    print(t.tableDelete(10))
    print(t.save())

    t.load({'type': 'sep', 'items': [[10], None, [2, 3], None, None]})
    t.tableInsert(createTableItem(15, 15))
    print(t.tableDelete(0))
    print(t.save())
    print(t.tableDelete(10))
    print(t.save())

