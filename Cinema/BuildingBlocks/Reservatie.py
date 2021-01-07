from Cinema.BuildingBlocks import _Foundation
import datetime


class Reservatie(_Foundation):
    def __init__(self, timestamp, user_id, vertoning_id, aantal_plaatsen):
        """
        id, een userid, een timestamp (tijd en datum), een vertoningid en een
        aantal plaatsen die gereserveerd worden. Blijft altijd bewaard. Zoeksleutel: id.

        :precondities: geen
        :postcondities: geen
        """
        self.vertoning_id: int = vertoning_id
        self.aantal_plaatsen: int = aantal_plaatsen
        self.timestamp: datetime.datetime = timestamp
        self.user_id: int = user_id
        self.id: int = 0

    def getVertoningId(self) -> int:
        """
        :return: geeft het vertoning id terug
        """
        return self.vertoning_id

    def getAantalPlaatsen(self) -> int:
        """
        :return: geeft het aantal plaatsen van een reservatie terug
        """
        return self.aantal_plaatsen

    def getTimeStamp(self) -> datetime.datetime:
        """
        :return: geeft de timestamp van de reservatie terug
        """
        return self.timestamp

    def getUserId(self) -> int:
        """
        :return: geeft het userid van de reservatie terug
        """
        return self.user_id

