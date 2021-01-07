from Cinema.BuildingBlocks import _Foundation


class Film(_Foundation):
    def __init__(self, id, titel, rating):
        """
        maakt de variabelen titel en rating
        :param titel: string (uniek)
        :param rating: 0 <= float <= 10
        :param id: int

        :precondities: geen
        :postcondities: geen
        """
        self.titel: str = titel
        self.rating: float = rating
        self.id: int = id

    def getTitel(self) -> str:
        """
        :return: return de titel van de film
        """
        return self.titel

    def getRating(self) -> float:
        """
        :return: return de rating van de film
        """
        return self.rating

