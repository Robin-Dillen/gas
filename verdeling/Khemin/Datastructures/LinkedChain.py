# Een node in de dubbelgelinkte lijst.
class Node:
    # Initialiseert een nieuw element van een dubbel gelinkte circulaire ketting. Ieder element heeft een next pointer
    # die naar het volgend element wijst, een previous pointer (prev) die naar het vorige element wijst, een value
    # attribuut die de waarde van het element bevat en een id attribuut die de zoeksleutel van value bevat. De ketting
    # is circulair doordat de next pointer van het laatste element naar het eerste element wijst en de previous pointer
    # van het eerste element naar het laatste element wijst.
    def __init__(self, id=None, value=None):
        self.id = id
        self.value = value
        self.next = self
        self.prev = self

### Een ADT voor een dubbelgelinkte circulaire ketting.
class LinkedChain:
    # Initialiseert de headpointer van de LinkedChain.
    def __init__(self, node = None):
        self.head = node

    # Een methode die weergeeft of de LinkedChain leeg is of niet.
    #
    # return: True
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    # Een methode die de lengte van de LinkedChain teruggeeft.
    #
    # return: Een positieve integer.
    def getLength(self):

        if self.isEmpty():
            return 0
        else:
            orig = self.head.id

            start = self.head.next
            length = 1
            while start.id != orig:
                length += 1
                start = start.next
            return length

    # Een methode die de LinkedChain doorloopt op zoek naar een item met het gegeven id.
    #
    # return: value, True als het item met gegegeven id in de LinkedChain aanwezig is, anders None, False.
    def retrieve(self, id):
        if self.isEmpty():
            return None, False

        orig = self.head
        if orig.value.getId() == id:
            return orig.value, True

        start = self.head.next
        while start != orig:
            if start.value.getId() == id:
                return start.value, True
            start = start.next

        return None, False

    # Een methode die de gelinkte ketting op zoeksleutel in volgorde doorloopt en een lijst teruggeeft met de elementen
    # in de gelinkte ketting in deze gesorteerde volgorde. Indien gewenst kan de volgorde ook geprint worden per element
    # door het extra argument print mee te geven.
    #
    # return: een lijst met de elementen uit de gelinkte ketting gesorteerd volgens zoeksleutel.
    def traverse(self, prt):
        lst = []
        for i in range(1, self.getLength() + 1):
            lst.append(self.retrieve(i))

        # if prt == print:
        #     for e in lst:
        #         print(e)

        for e in lst:
            prt(e)

        return lst


    # Een methode die de grootste zoeksleutel in de LinkedChain teruggeeft door de ketting te doorlopen.
    #
    # return: De grootste zoeksleutel wordt teruggegeven indien er een grootste zoeksleutel aanwezig is, anders wordt
    # None teruggegeven.
    def largest_key(self):
        if self.isEmpty():
            return 0
        else:
            orig = self.head.id

            largest = self.head.id

            start = self.head.next
            while start.id != orig:
                if start.id > largest:
                    largest = start.id
                start = start.next

            return largest

    # Een methode die een nieuw element toevoegd aan de LinkedChain.
    #
    # return: True in dien het inserten gelukt is, anders False.
    def insert(self, place, value):

        if place > self.getLength() + 1:
            return False

        if self.isEmpty():
            self.head = Node(place, value)
            return True

        else:
            if place < self.getLength():
                start = self.head
                while start.id != place:
                    start = start.next
                new = Node(place, value)
                if place == 1:
                    self.head = new
                start.id += 1
                new.prev = start.prev
                start.prev = new
                new.next = start
                new.prev.next = new
                while start.id != self.getLength() and start != new:
                    start.id += 1
                    start = start.next
                return True


            else:
                start = self.head
                while start.id != place - 1:
                    start = start.next
                new = Node(place, value)
                new.next = start.next
                start.next = new
                new.prev = start
                new.next.prev = new

                return True

    # Verwijdert het element met het gegeven id uit de LinkedChain.
    #
    # return: True als het verwijderen gelukt is, anders False.
    def delete(self, id):
        if not self.retrieve(id)[1]:
            return False

        l = self.getLength()

        start = self.head
        while start.id != id:
            start = start.next

        if id == 1:
            self.head = start.next
            start.prev.next = start.next
            start.next.prev = start.prev
            start = start.next
            while start.id <= l:
                if start.id < l:
                    start.id -= 1
                    start = start.next
                else:
                    start.id -= 1
                    break
            return True
        else:
            start.prev.next = start.next
            start.next.prev = start.prev
            if start.next != start.prev:
                start = start.next
                while start.id <= l:
                    if start.id < l:
                        start.id -= 1
                        start = start.next
                    else:
                        start.id -= 1
                        break
            return True


    # Een methode die de LinkedChain saved door een lijstrepresentatie van de LinkedChain op te
    # stellen en deze als output terug te geven.
    # return: Een lijst met de elementen van de LinkedChain.
    def save(self):
        start = self.head
        orig = start.id
        saved = [start.value]

        start = start.next
        while start.id != orig:
            saved.append(start.value)
            start = start.next

        return saved

    # Een methode die een nieuwe LinkedChain inlaadt adv een lijstrepresentatie.
    # post: self is herschreven en bevat de elementen vanuit de lijstrepresentatie.
    def load(self, lst):
        self.head = Node(1, lst[0])
        key = 2
        for e in lst[1:]:
            self.insert(key, e)
            key += 1


class LinkedChainTable(LinkedChain):

    def __init__(self):
        super().__init__()

    def tableIsEmpty(self):
        return self.isEmpty()

    def tableLength(self):
        return self.getLength()

    def tableInsert(self,place,value):
        return self.insert(place,value)

    def tableDelete(self, key):
        return self.delete(key)

    def tableRetrieve(self,id):
        return self.retrieve(id)

    def traverseTable(self, prt):
        return self.traverse(prt)


# Een functie die een snelle visualitatie van de LinkedChain geeft. Er wordt per element in de gelinkte ketting
# een regel naar de console geprint. Deze regels zijn van de vorm: a | b c. Hierbij is a het id van het element zelf, b
# het id van de prev pointer en c het id van de next pointer.
def print_chain(chain):
    orig = chain.id
    print(chain.id,'|', chain.prev.id, chain.next.id)
    start = chain.next

    while start.id != orig:
        print(start.id, '|', start.prev.id, start.next.id)
        start = start.next


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
