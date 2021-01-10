class Queue:
    def __init__(self, length=0):
        self.length = length
        self.list = []

    def load(self, list):
        """
        Laadt een Queue in
        :param list: Lijst van items
        :return: True als het gelukt is
        precondition: None

        postcondition: None
        """
        self.list = list
        return True

    def isEmpty(self):
        """
        bepaalt of een queue leeg is
        :param self.list = lijst met Queue's
        :return False als de lijst niet leeg is en True als de lijst wel leeg is

        precondition:  self.list moet een lijst zijn

        postcondition: None
        """
        if (len(self.list) == 0):
            return True
        else:
            return False

    def enqueue(self, key):
        """
        voegt een element toe aan de queue
        :param value = waarde van item dat wordt toegevoegd aan de queue
        :param self.list = lijst met Queue's
        :return False als het mislukt is en True als het gelukt is

        precondition: None

        postcondition: lengte van de queue moet vergoten met 1
        """
        if (self.length > len(self.list)):
            self.list.insert(0, key)
            return True
        return False

    def dequeue(self):
        """
        verwijdert het eerst toegevoegde element uit de queue
        :param self.list = lijst met Queue's
        :return False als het mislukt is en True als het gelukt is


        precondition: lijst van queue mag niet leeg zijn

        postcondition: lengte van de queue moet verkleinen met 1
        """
        if (len(self.list) == 0):
            return False, False
        a = self.list[len(self.list) - 1]
        del self.list[len(self.list) - 1]
        return a, True

    def getFront(self):
        """
        vraagt het eerst toegevoegde element uit de queue op
        :param self.list = lijst met Queue's
        :return Tuple met item dat eerst is toegevoegd

        precondition: self.list.queue mag niet leeg zijn

        postcondition: None
        """
        if (len(self.list) == 0):
            return False, False
        return self.list[len(self.list) - 1], True

    def save(self):
        """
        slaat een queue op
        :return: lijst met alle items van de queue

        precondition: None

        postcondition: None
        """
        l = []
        for i in self.list:
            l.append(i)
        return l

if __name__ == "__main__":
    q = Queue(10)
    print(q.isEmpty())
    print(q.getFront()[1])
    print(q.dequeue()[1])
    print(q.enqueue(2))
    print(q.enqueue(4))
    print(q.isEmpty())
    print(q.dequeue()[0])
    q.enqueue(5)
    print(q.save())

    q.load(['a', 'b', 'c'])
    print(q.save())
    print(q.dequeue()[0])
    print(q.save())
    print(q.getFront()[0])
    print(q.save())
