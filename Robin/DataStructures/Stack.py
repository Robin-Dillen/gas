from .LinkedChain import LinkedChain
from typing import Tuple


class Stack:
    def __init__(self) -> None:
        self.stack = LinkedChain()

    def isEmpty(self) -> bool:
        """
        :return: geeft True terug als de stack leeg is
        """
        return self.stack.isEmpty()

    def push(self, newItem: any) -> bool:
        """
        voegt een element toe aan de top stack
        :param newItem: object dat opgeslagen moet worden
        :return: Succes als het gelukt is
        :pre geen
        :post de grootte van de stack is met 1 vermeerdert
        """
        return self.stack.insert(self.stack.getLength() + 1, newItem)

    def pop(self) -> Tuple[any, bool]:
        """
        verwijdert de top van de stack en geeft het element terug
        :return: top van de stack, succes als het gelukt is
        :pre geen
        :post er zit een element minder in de stack
        """
        top = self.stack.retrieve(self.stack.getLength())
        self.stack.delete(self.stack.getLength())
        return top

    def getTop(self) -> Tuple[any, bool]:
        """
        :return: geeft de top van de stack terug
        :pre geen
        :post de stack is niet aangepast
        """
        return self.stack.retrieve(self.stack.getLength())

    def save(self) -> list:
        """
        slaagt de stack op in een lijst
        :return: lijst met elementen
        """
        return self.stack.save()

    def load(self, stack: list) -> None:
        """
        maakt de stack leeg en laadt een lijst in met elementen
        :param stack: lijst met elementen (eerste item eerst)
        :return: None
        """
        self.stack.load(stack)



