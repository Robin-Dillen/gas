from Cinema.DataStructures.LinkedChain import LinkedChain
from typing import Tuple


class Queue:
    def __init__(self):
        self.queue: LinkedChain = LinkedChain()

    def isEmpty(self) -> bool:
        """
        geeft True terug als de queue leeg is ander False
        :return: Bool
        :precondities: geen
        :postconditites: geen
        """
        return self.queue.isEmpty()

    def enqueue(self, newItem: any) -> bool:
        """
        voegt een element achteraan toe aan de queue
        :param newItem: item dat toegevoegt moet worden
        :return: Succes

        :precondities: geen
        :postconditites: de queue bevat een obj meer, geeft True terug als het gelukt is anders False
        """
        return self.queue.insert(1, newItem)

    def dequeue(self) -> Tuple[object, bool]:
        """
        searchTreeDelete het eerste obj uit de lijst
        :return: het obj

        :precondities: geen
        :postconditites: de queue bevat een obj minder, geeft True terug als het gelukt is anders False
        """
        front = self.queue.retrieve(self.queue.getLength())
        self.queue.delete(self.queue.getLength())
        return front

    def getFront(self) -> Tuple[object, bool]:
        """
        geeft het eerste element in de stack terug
        :return: front
        :precondities: geen
        :postconditites: geen
        """
        return self.queue.retrieve(self.queue.getLength())

    def getSize(self) -> int:
        """
        geeft de grootte van de queue terug
        :return: size

        :precondities: geen
        :postconditites: geen
        """
        return self.queue.getLength()

    def save(self) -> list:
        """
        geeft de queue terug als lijst
        :return: lijst
        """
        return self.queue.save()

    def load(self, items: list) -> None:
        """
        loaad een lijst van elementen in
        :param items:
        :return:
        """
        self.queue.load(items)


if __name__ == "__main__":
    q = Queue()
    print(q.isEmpty())  # True
    print(q.getFront()[1])  # False
    print(q.dequeue()[1])  # False
    print(q.enqueue(2))  # True
    print(q.enqueue(4))  # True
    print(q.isEmpty())  # False
    print(q.dequeue()[0])  # 2
    q.enqueue(5)
    print(q.save())  # [5, 4]
    q.load(['a', 'b', 'c'])
    print(q.save())  # ['a', 'b', 'c']
    print(q.dequeue()[0])  # c
    print(q.save())  # ['a', 'b']
    print(q.getFront()[0])  # b
    print(q.save())  # ['a', 'b']
