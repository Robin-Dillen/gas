### Deze ADT stelt een Queue voor. Items worden vooraan verwijderd en achteraan toegevoegd.
# De naam is hier niet gewoonweg Queue omdat dit een klasse die de debugger gebruikt overschrijft waardoor de debugger niet meer runt.

class ADTQueue:

    # Creërt een nieuwe lege queue.
    # self.items wordt geïnitialiseerd op een lege lijst, self.front en self.back zijn None.
    def __init__(self, maxl=100):
        self.items = []
        self.maxl = maxl
        self.front = None
        self.back = None

    # Geeft aan of de queue leeg is of niet.
    # return:
    #     True wordt teruggegeven als de queue leeg is, anders wordt False teruggegeven.
    def isEmpty(self):
        return len(self.items) == 0

    # Voegt een item toe achteraan de queue, update hierbij de back van de queue naar het ingevoegde element en geeft aan of het
    # toevoegen gelukt is (success).
    # param:
    #     item : het item dat aan de queue wordt toegevoegd.
    # post:
    #    De queue is in lengte toegenomen met 1.
    #    De back van de queue is gelijk aan het toegevoegde item.
    # return:
    #    success : Geeft weer of het toevoegen gelukt is of niet adv een True of False.
    def enqueue(self, item):
        if self.isEmpty():
            self.items.append(item)
            self.front = item
            self.back = item
        elif len(self.items) < self.maxl:
            self.items.append(item)
            self.back = item

        if self.items[-1] == item:
            return True
        else:
            return False

    # Verwijdert de front van de queue uit de queue en geeft dit item terug. Hierbij wordt de front van de queue geüpdated
    # naar het item net na het verwijderde item in de stack. In een tuple wordt het verwijderde item teruggegeven samen
    # met succes (i, success). Als het item niet verwijderd werd, wordt enkel succes teruggegeven.
    # post:
    #    De queue is in lengte afgenomen met 1.
    #    De front van de queue is nog steeds het voorste element van de nu kortere queue.
    # return:
    #    i : Het verwijderde item.
    #    success : Geeft weer of het verwijderen gelukt is of niet adv een True of False.
    def dequeue(self):
        i = None
        if not self.isEmpty():
            i = self.items.pop(0)
            if not self.isEmpty():
                self.front = self.items[0]
            else:
                self.front = None
                self.back = None
        if i is not None:
            return (i, True)
        else:
            return (i, False)

    # Geeft het item in de front van de queue terug en geeft weer of dit gelukt is via succes. Dit gebeurt als een tuple (front, success)
    # post:
    #    Er is niets gewijzigd aan de queue.
    # return:
    #    front : Het item aan de front van de queue zit.
    #    success : Geeft weer of het ophalen van de front van de queue gelukt is of niet adv een True of False.
    def getFront(self):
        if self.front is not None:
            return (self.front, True)
        else:
            return (self.front, False)

    # Geeft het item aan de back van de queue terug en geeft weer of dit gelukt is via succes. Dit gebeurt als een tuple (back, success)
    # post:
    #    Er is niets gewijzigd aan de queue.
    # return:
    #    back : Het item aan de back van de queue.
    #    success : Geeft weer of het ophalen van de back van de queue gelukt is of niet adv een True of False.
    def getBack(self):
        if self.back is not None:
            return (self.back, True)
        else:
            return (self.back, False)

    # Een methode die de queue saved door een lijstrepresentatie van de queue op te stellen en deze als output terug
    # te geven.
    # return: Een lijst met de elementen van de queue. De back van de queue staat vooraan in de lijst en
    # de front van de queue staat achteraan.
    def save(self):
        saved = [self.getFront()[0]]
        for e in self.items[1:]:
            saved.insert(0, e)
        return saved

    # Een methode die een nieuwe Stack inlaadt adv een lijstrepresentatie.
    # post: self is herschreven en bevat de elementen vanuit de lijstrepresentatie.
    def load(self, lst):
        self.maxl = len(lst)
        self.items = []
        i = -1
        while i >= -len(lst):
            self.enqueue(lst[i])
            i -= 1
