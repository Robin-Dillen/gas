class Stack:
    def __init__(self, length=0):
        self.length = length
        self.list = []

    def load(self, list):
        """
        Laadt een stack in
        :param list: Lijst van items
        :return: True als het gelukt is
        """
        self.list = list
        return True

    def isEmpty(self):
        """
        bepaald of een stack leeg is
        :param self.list = lijst met stacks
        :return False als de lijst niet leeg is en True als de lijst wel leeg is

        precondition:  self.list moet een lijst zijn

        postcondition: None
        """
        if (len(self.list) == 0):
            return True
        else:
            return False

    def push(self, value):
        """
        voegt een element toe aan de stack
        :param value = item dat moet worden toegevoegd
        :return False als het mislukt is en True als het gelukt is

        precondition: lijst van stack mag niet leeg zijn

        postcondition: lengte van de stack moet vergroten met 1
        """
        if (self.length > len(self.list)):
            self.list.append(value)
            return True
        return False

    def pop(self):
        """
        verwijdert het laatst toegevoegde element uit de stack
        :param self.list = lijst met stacks
        :return False als het mislukt is en True als het gelukt is

        precondition: lijst van stack mag niet leeg zijn

        postcondition: lengte van de stack moet verkleinen met 1
        """
        if (len(self.list) == 0):
            return False, False
        a = self.list[len(self.list) - 1]
        del self.list[len(self.list) - 1]
        return a, True

    def getTop(self):
        """
        vraagt het laatst toegevoegde element uit de stack op
        :param self.list = lijst met stacks
        :return Tuple met item dat laatst is toegevoegd

        precondition: self.list.stack mag niet leeg zijn

        postcondition: None
        """
        if (len(self.list) == 0):
            return False, False
        return self.list[len(self.list) - 1], True

    def save(self):
        """
        slaat een stack op
        :return: lijst met alle elementen van de stack7

        precondition: None

        postcondition: None
        """
        l = []
        for i in self.list:
            l.append(i)
        return l


s = Stack(2)
print(s.isEmpty())
print(s.getTop()[1])
print(s.pop()[1])
print(s.push(2))
print(s.push(4))
print(s.push(1))
print(s.isEmpty())
print(s.pop()[0])
s.push(5)
print(s.save())

s.load(['a', 'b', 'c'])
print(s.save())
print(s.pop()[0])
print(s.save())
print(s.getTop()[0])
print(s.save())
