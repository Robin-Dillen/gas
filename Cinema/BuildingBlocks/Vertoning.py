from datetime import datetime
from Cinema.BuildingBlocks import _Foundation
from Cinema import clock


class Vertoning(_Foundation):
    def __init__(self, id, zaalnummer, tijdsslot, datum, film_id, totaal_aantal_plaatsen):
        """
         bevat een id, een zaalnummer, een slot, een datum, een filmid, aantal vrije
        plaatsen. Zoeksleutel: id.
        :param zaalnummer: int groter dan 0
        :param tijdsslot: datetime.timedelta object
        :param datum: datetime.datetime
        :param film_id: film object
        :param aantal_vrije_plaatsen: 0 < int

        :precondities: geen
        :postcondities: geen
        """
        self.id = id
        self.zaalnummer: int = zaalnummer
        self.tijdsslot: datetime = tijdsslot
        self.datum = datum
        self.film_id = film_id
        self.aantal_vrije_plaatsen = totaal_aantal_plaatsen
        self.aantal_mensen_zaal = 0
        self.aantal_reservaties = 0

    def getZaalnummer(self) -> int:
        """
        :return: geeft het zaalnummer terug
        """
        return self.zaalnummer

    def getTijdsslot(self) -> datetime:
        """
        :return: geeft het tijdsslot van de vertoning terug
        """
        return self.tijdsslot

    def getDatum(self) -> datetime:
        """
        :return: geeft de datum terug
        """
        return self.datum

    def getFilmId(self) -> int:
        """
        :return: geeft het film id terug
        """
        return self.film_id

    def getVrijePlaatsen(self) -> int:
        """
        :return: geeft het aantal vrije plaatsen terug
        """
        return self.aantal_vrije_plaatsen

    def updateReservaties(self, x) -> None:
        """
        trek x af va, het aantal vrije plaatsen
        :param x:  int
        :return: None
        """
        self.aantal_vrije_plaatsen -= x
        self.aantal_reservaties += x

    def addAantalMensenZaal(self, x: int):
        """
        voeg x mensen toe aan de mensen in de zaal
        """
        self.aantal_mensen_zaal += x

    def IsStarted(self):
        """
        geeft True terug als de film begonnen is
        :return: bool
        :precondities: geen
        :postcondities: geen
        """
        return self.tijdsslot > clock.getTime()

    def wachtendOp(self):
        """
        :return: geeft terug op hoeveel mensen er gewacht moet worden
        """
        return self.aantal_mensen_zaal - self.aantal_reservaties

    def toString(self):
        if self.IsStarted():
            if self.wachtendOp() == 0:
                return "F:" + str(self.aantal_mensen_zaal)
            else:
                return "W:" + str(self.aantal_reservaties - self.aantal_mensen_zaal)

        return "G:" + str(self.aantal_reservaties)
