class _Foundation:
    """super class, private"""

    def getSearchKey(self) -> int:
        """
        :return: geeft het id van de subclass terug

        :precondities: geen
        :postcondities: geen
        """
        return self.id

    def __eq__(self, other):
        return self.id == other if isinstance(other, int) else self.id == other.id

    def __ne__(self, other):
        return self.id != other if isinstance(other, int) else self.id != other.id

    def __gt__(self, other):
        return self.id > other if isinstance(other, int) else self.id > other.id

    def __ge__(self, other):
        return self.id >= other if isinstance(other, int) else self.id >= other.id

    def __lt__(self, other):
        return self.id < other if isinstance(other, int) else self.id < other.id

    def __le__(self, other):
        return self.id <= other if isinstance(other, int) else self.id <= other.id


from .Film import Film
from .Gebruiker import Gebruiker
from .Zaal import Zaal
from .Vertoning import Vertoning
from .Reservatie import Reservatie
