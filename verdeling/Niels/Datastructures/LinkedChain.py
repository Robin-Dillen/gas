
class LinkedChain:
    def __init__(self):
        self.list = [None]

    def load(self,list):
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

    def add(self,value):
        """
        voegt een item toe op het einde van de ketting
        :param value: waarde van het item
        :return: none

        precondition: None

        postcondition: None
        """
        self.list.append(value)

    def insert(self,index,value):
        """
        voegt een item toe op potitie index
        :param value: waarde van het item
        :param index: plaats waar het item moet worden toegevoegd
        :return: none

        precondition: None

        postcondition: None
        """
        if(len(self.list)>=index):
            self.list.insert(index,value)
            return True
        else: return False

    def delete(self,index):
        """
        verwijdert een item uit de ketting
        :param index: plaats waar het item moet worden verwijderd
        :return: none

        precondition: de gegeven index/value moet bestaan in de ketting

        postcondition: lengte van de ketting zal verkleinen met 1
        """
        if(index > 0):
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
        return len(self.list)-1

    def get_next_item(self,index):
        """
        geeft de lengte van het volgende item weer
        :param index: index van het opgegeven item
        :return: none

        precondition: lengte van de Ketting moet groter zijn dan 0

        postcondition: None
        """
        if(index == len(self.list)-1):
            return self.list[0]
        else: return self.list[index+1]

    def get_previous_item(self,index):
        """
        geeft de lengte van het vorige item weer
        :param index: index van het opgegeven item
        :return: none

        precondition: lengte van de Ketting moet groter zijn dan 0

        postcondition: None
        """
        if(index == 0):
            return self.list[-1]
        else: return self.list[index-1]

    def isEmpty(self):
        """
        Kijkt na of een ketting leeg is
        :return: True als het leeg is, false als het niet leeg is

        precondition: None

        postcondition: None
        """
        if(len(self.list) == 1):
            return True
        else: return False

    def retrieve(self,index):
        """
        Geeft een item terug op de gevraagde index
        :param index: index van het gevraagde item
        :return: (Item, True) als het de index geldig is, (false,false) als dat niet zo is
        precondition: None

        postcondition: None
        """
        if(self.getLength() >= index):
            return self.list[index],True
        else: return False,False

    def save(self):
        """
        slaat een ketting op
        :return: lijst met alle items van een ketting

        precondition: None

        postcondition: None
        """
        l = []
        for i in range(1,len(self.list)):
            l.append(self.list[i])
        return l


class LinkedChainTable:
    def __init__(self):
        self.a = LinkedChain()

    def load(self,tree):
        self.a.load(tree)

    def tableInsert(self,index,value):
        return self.a.insert(index,value)

    def tableDelete(self,value):
        return self.a.delete(value)

    def tableLength(self):
        return self.a.getLength()

    def tableIsEmpty(self):
        return self.a.isEmpty()

    def tableRetrieve(self,index):
        return self.a.retrieve(index)

    def save(self):
        return self.a.save()
