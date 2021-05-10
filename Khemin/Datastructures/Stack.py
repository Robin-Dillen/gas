### Deze ADT stelt een stack voor. Items worden bovenaan ingevoegd en verwijderd.
class Stack:

    # Creërt een nieuwe lege stack.
    # self.items wordt geïnitialiseerd op een lege lijst, self.top is None.
    def __init__(self, maxl):
        self.items = []
        self.maxl = maxl
        self.top = None

    # Geeft aan of de stack leeg is of niet.
    # return:
    #     True wordt teruggegeven als de stack leeg is, anders wordt False teruggegeven.
    def isEmpty(self):
        return len(self.items) == 0

    # Voegt een item toe vooraan de stack, update hierbij de top van de stack naar het ingevoegde element en geeft aan of het
    # toevoegen gelukt is (success).
    # param:
    #     item : het item dat aan de stack wordt toegevoegd.
    # post:
    #    De stack is in lengte toegenomen met 1.
    #    De top van de stack is gelijk aan het toegevoegde item.
    # return:
    #    success : Geeft weer of het toevoegen gelukt is of niet adv een True of False.
    def push(self, item):
        if len(self.items) < self.maxl:
            self.items.insert(0, item)
            self.top = item

        if self.items[0] == item:
            return True
        else:
            return False

    # Verwijdert de top van de stack uit de stack en geeft dit item terug. Hierbij wordt de top van de stack geüpdated
    # naar het item net na het verwijderde item in de stack. In een tuple wordt het verwijderde item teruggegeven samen
    # met succes (i, success). Als het item niet verwijderd werd, wordt enkel succes teruggegeven.
    # post:
    #    De stack is in lengte afgenomen met 1.
    #    De top van de stack is nog steeds het bovenste element van de nu kortere stack.
    # return:
    #    i : Het verwijderde item.
    #    success : Geeft weer of het verwijderen gelukt is of niet adv een True of False.
    def pop(self):
        i = None
        if not self.isEmpty():
            i = self.items.pop(0)
            if not self.isEmpty():
                self.top = self.items[0]
            else:
                self.top = None
        if i is not None:
            return (i, True)
        else:
            return (i, False)

    # Geeft het item op de top van de stack terug en geeft weer of dit gelukt is via succes. Dit gebeurt als een
    # tuple (top, success).
    # post:
    #    Er is niets gewijzigd aan de stack.
    # return:
    #    top : Het item op de top van de stack.
    #    success : Geeft weer of het ophalen van de top van de stack gelukt is of niet adv een True of False.
    def getTop(self):
        if self.top is not None:
            return (self.top, True)
        else:
            return (self.top, False)

    # Een methode die de stack saved door een lijstrepresentatie van de stack op te stellen en deze als output terug
    # te geven.
    # return: Een lijst met de elementen van de stack. Het onderste element in de stack staat vooraan in de lijst en
    # de top van de stack staat achteraan.
    def save(self):
        saved = []
        for e in self.items:
            if len(saved) == 0:
                saved.append(e)
            else:
                saved.insert(0, e)
        return saved

    # Een methode die een nieuwe Stack inlaadt adv een lijstrepresentatie.
    # post: self is herschreven en bevat de elementen vanuit de lijstrepresentatie.
    def load(self, lst):
        self.maxl = len(lst)
        self.items = []
        for e in lst:
            self.push(e)