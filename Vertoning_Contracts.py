"""Deze ADT stelt een vertoning voor.
Een vertoning wordt gedefineerd door een unieke id (zoeksleutel).
Verder heeft een vertoning nog een zaalnummer, een slot, een datum, een filmid
en een aantal vrije plaatsen.
"""
from datetime import datetime
import threading
from Clock import clock


class Vertoning:

    def __init__(self, id, zaalnummer, slot, datum, filmid, aantal_vrij):
        """
        Initialiseert een nieuwe vertoning met de opgegeven id, zaalnummer, slot, datum, filmid en aantal_vrij.
        :param id : de unieke id van de vertoning
        :param zaalnummer : het zaalnummer van de zaal waar de vertoning gespeeld wordt.
        :param slot : Het tijdstip waarop de vertoning gespeeld wordt.
        :param datum : het datum waarop de vertoning gespeeld wordt.
        :param filmid : het id van de film die gespeeld zal worden tijdens de vertonging.
        :param aantal_vrij : het aantal vrije plaatsen in de zaal van de vertoning
        :return: geen

        preconditie:
            De meegegeven id is een positieve integer.
            De meegegeven zaalnummer is een positieve integer.
            Het meegegeven slot is een string.
            De meegegeven datum is een string.
            De meegegeven filmid is een positieve integer.
            De meegegeven aantal_vrij is een positieve integer.

        postconditie: geen
        """
        self.id_ = id
        self.zaalnummer = zaalnummer
        self.slot = slot
        self.datum = datum
        self.filmid = filmid
        self.aantal_vrij = aantal_vrij
        self.aantal_mensen_binnen = 0
        self.playing = False

    def getId(self):
        """
        Een functie die de waarde van id teruggeeft.

        preconditie: geen

        postconditie: De gebruiker is niet veranderd.
        """
        return self.id_

    def getSlot(self) -> datetime.time:
        """
        Een functie die de slot teruggeeft.

        preconditie: geen

        postconditie: De gebruiker is niet veranderd.
        """
        return self.slot

    def getDatum(self) -> datetime.date:
        """
        Een functie die de datum teruggeeft.

        preconditie: geen

        postconditie: De gebruiker is niet veranderd.
        """
        return self.datum

    def getAantalVrij(self):
        """
        Een functie die de aantal_vrij teruggeeft.

        preconditie: geen

        postconditie: De gebruiker is niet veranderd.
        """
        return self.aantal_vrij

    def setId(self, value):
        """
        Een functie die de id update naar de gegeven waarde.
        :param value: de nieuwe waarde van id

        preconditie: De gegeven value is een positieve integer.

        postconditie: De waarde van id is geüpdatet naar de gegeven value.
        """
        self.id = value

    def getZaalnummer(self):
        """
        Een functie die de zaalnummer teruggeeft.
        preconditie: geen
        postconditie: De gebruiker is niet veranderd.
        """
        return self.zaalnummer

    def setZaalnummer(self, value):
        """
        Een functie die de zaalnummer update naar de gegeven waarde.
        :param value: de nieuwe zaalnummer

        preconditie: De gegeven value is een positieve integer.

        postconditie: De waarde van id is geüpdatet naar de gegeven value.
        """
        self.zaalnummer = value

    def setSlot(self, value):
        """
        Een functie die de slot update naar de gegeven waarde.
        :param value: het nieuwe slot

        preconditie: De gegeven value is een string.

        postconditie: De slot is geüpdatet naar de gegeven value.
        """
        self.slot = value

    def setDatum(self, value):
        """
        Een functie die de datum update naar de gegeven waarde.
        :param value: de nieuwe datum

        preconditie: De gegeven value is een string.

        postconditie: De datum is geüpdatet naar de gegeven value.
        """
        self.datum = value

    def getFilmId(self):
        """
        Een functie die de filmid teruggeeft.
        preconditie: geen
        postconditie: De gebruiker is niet veranderd.
        """
        return self.filmid

    def setFilmId(self, value):
        """
        Een functie die de filmid update naar de gegeven waarde.
        :param value: de nieuwe filmid

        preconditie: De gegeven value is een positieve integer.

        postconditie: De filmid is geüpdatet naar de gegeven value.
        """
        self.filmid = value

    def setAantalVrij(self, value):
        """
        Een functie die de aantal_vrij update naar de gegeven waarde.
        :param value: het nieuwe aantal vrije plaatsen in de zaal van de vertoning

        preconditie: De gegeven value is een positieve integer.

        postconditie: De aantal_vrij is geüpdatet naar de gegeven value.
        """
        self.aantal_vrij = value

    def start(self):
        """
        Een methode die een vertoning start door het playing attribuut op True te zetten.
        :return: Als de vertoning al aan het spelen is wordt er False teruggegeven. Al de start succesvol was wordt er True teruggegeven.

        preconditie: geen

        postconditie: geen
        """
        self.playing = True

    def stop(self):
        """
        Een methode die een vertoning stopt door het playing attribuut op False te zetten.
        :return: Als de vertoning niet aan het spelen is wordt er False teruggegeven. Al de stop succesvol was wordt er True teruggegeven.

        preconditie: geen

        postconditie: geen
        """
        self.playing = False

    def isStarted(self):
        """
        geetf terug of de film aan het spelen is
        :return: True als de film aan het spelen is ander False
        """
        return self.playing

    def isWaiting(self):
        """geeft True terug als de vertoning aan het wachten is op mensen"""
        return datetime.combine(self.datum, self.slot) <= clock.getTime() and not self.isStarted()

    def getAantalMensenBinnen(self):
        """geeft terug hoeveel mensen in de zaal zitten"""
        return self.aantal_mensen_binnen

    def setAantalMensenBinnen(self, new_aantal):
        """update de waarde van self.aantal_mensen_binnen naar new_aantal"""
        self.aantal_mensen_binnen = new_aantal
