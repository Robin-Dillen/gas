from Cinema.BuildingBlocks import _Foundation


class Zaal(_Foundation):
    def __init__(self, nummer, aantal_plaatsen):
        """
        bevat een nummer en het aantal plaatsen. Zoeksleutel: nummer

         :precondities: geen
        :postcondities: geen
        """
        self.id = nummer
        self.aantal_plaatsen = aantal_plaatsen

    def getAantalPlaatsen(self) -> int:
        """
        :return: geeft het aantal plaatsen terug
        """
        return self.aantal_plaatsen

