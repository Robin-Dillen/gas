"""
Deze ADT stelt het beheer van het volledige reservatiesysteem voor.
Het bevat verschillende functies om de kleiner ADT's (Film, Gebruiker,
Reservatie, Vertoning, Zaal) samen te brengen in een groter geheel.
"""
from Film_Contracts import Film
from Gebruiker_Contracts import Gebruiker
from Reservatie_Contracts import Reservatie
from Vertoning_Contracts import Vertoning
from Zaal_Contracts import Zaal

from DataStructures import BSTTable, LinkedChainTable, RedBlackTreeTable, Queue


class Reservatiesysteem:
    def __init__(self, films=LinkedChainTable(), gebruikers=LinkedChainTable(),
                 reservaties=Queue(), vertoningen=BSTTable(),
                 zalen=LinkedChainTable()):

        self.films = films
        self.gebruikers = gebruikers
        self.reservaties = reservaties
        self.vertoningen = vertoningen
        self.zalen = zalen
        self.tijd = 0

    def retrieve_vertoningen(self, id):  # maker Khemin, tester Niels
        """
        Een functie die uit een datastructuur van objecten het object haalt met het opgegeven id.
        Het object wordt teruggegeven indien het gevonden wordt in het ADT. Als het niet in de ADT zit wordt er None teruggegeven.
        :param id: id van het object, is een positieve integer.
        :return:  Object
        post: De gegeven lst is niet van inhoud en/of lengte veranderd.
        """
        return self.vertoningen.tableRetrieve(id)

    def maakAccount(self, voornaam="", achternaam="", email=""):  # maker Niels, tester Robin
        """
        Een functie die voor de gegeven voornaam,achternaam en e-mailadres een
        nieuw gebruiker aanmaakt en deze toevoegd aan het ADT van gebruiker van het reservatiesysteem.
        :param voornaam: de voornaam van de nieuwe gebruiker, is een string.
        :param achternaam: de achternaam van de nieuwe gebruiker, is een string.
        :param email: het e-mailadres van de nieuwe gebruiker, is een string.
        :return: Het id van de nieuwe gebruiker wordt teruggegeven.
        """
        gebruiker = Gebruiker(voornaam, achternaam, email)
        self.gebruikers.tableInsert(self.gebruikers.tableLength(), gebruiker)
        return True

    def addFilm(self, id, titel, rating):  # maker Robin, tester Khemin
        """
        Een functie die voor de gegeven titel en rating een
        nieuw film aanmaakt en deze toevoegd aan het ADT van films van het reservatiesysteem.
        :param titel: de titel van de film, is een string.
        :param rating: de rating van de film, is een float tussen 1-10.
        :return: Het id van de nieuwe film wordt teruggegeven.
        """
        film = Film(id, titel, rating)
        self.films.tableInsert(self.films.tableLength(), film)
        print(f"The movie {titel} has been created!")
        return True

    def addReservatie(self, userid=0, timestamp=object, vertoningid=0, plaatsen=0):  # maker Khemin, tester Niels
        """
        Een functie die voor de gegeven userid, timestamp, vertoninging en plaatsen een nieuw reservatie aanmaakt en deze toevoegd aan het ADT van reservaties van het reservatiesysteem.
        :param userid : de userid van de gebruiker die de reservatie aangemaakt heeft.
        :param timestamp : Het tijdstip waarop de reserveerde vertoning gespeeld wordt.
        :param vertoningid : het id van de vertoning die gereserveerd werd.
        :param plaatsen : het aantal plaatsen dat gereserveerd wordt
        :return: Het id van de nieuwe reservatie wordt teruggegeven.

        preconditie:
            De meegegeven titel is een string.
            De meegegeven userid is een positieve integer.
            De meegegeven timestamp is een tuple met twee strings als elementen. De eerste string geeft het tijdstip van reservatie weer, de tweede geeft de reservatiedatum weer.
            De meegegeven vertoningid is een positieve integer.
            De meegegeven plaatsen is een positieve integer.

        postconditie: geen
        """
        self.reservaties.enqueue(Reservatie(userid, timestamp, vertoningid, plaatsen))

    def addVertoning(self, zaalnummer=0, slot=object, datum=object, filmid=0,
                     aantal_vrij=0):  # maker Niels, tester Robin
        """
        Een functie die voor de gegeven zaalnummer, slot, datum, filmid en aantal_vrij een
        nieuw vertoning aanmaakt en deze toevoegd aan het ADT van vertoningen van het reservatiesysteem.
        :param zaalnummer: het zaalnummer van de zaal waar de vertoning gespeeld wordt., is een positieve integer.
        :param slot: Het tijdstip waarop de vertoning gespeeld wordt, is een datetime.timedelta.
        :param datum: het datum waarop de vertoning gespeeld wordt, is een datetime.datime object.
        :param filmid: het id van de film die gespeeld zal worden tijdens de vertonging, is een positieve integer.
        :param aantal_vrij: het aantal vrije plaatsen in de zaal van de vertoning, is een positieve integer.
        :return: Het id van de nieuwe vertoning wordt teruggegeven.
        """
        vertoning = Vertoning(zaalnummer, slot, datum, filmid, aantal_vrij)
        self.vertoningen.tableInsert(self.vertoningen.tableLength(), vertoning)
        return True

    def updateTicketten(self, vertoning_id, ticketten):
        """
        Als mensen binnenkomen bij de vertoning worden de ticketten afgetrokken
        :param vertoning_id: id van de vertoning
        :param ticketten: aantal mensen dat binnenkomt
        :return: true als succes
        """
        vertoning : Vertoning
        vertoning, succes = self.vertoningen.tableRetrieve(vertoning_id)
        if succes:
            vertoning.setAantalMensenBinnen(vertoning.getAantalMensenBinnen() - ticketten)
            zaal : Zaal
            zaal, succes = self.zalen.tableRetrieve(vertoning.getZaalnummer())
            if succes and vertoning.getAantalMensenBinnen() + vertoning.getAantalVrij() == zaal.getPlaatsen():
                vertoning.start()
            return True
        return False

    def addZaal(self, id_, plaatsen) -> bool:  # maker Robin, tester Khemin
        """
        Een functie die voor de gegeven titel en rating een nieuwe zaal aanmaakt en deze toevoegd aan het ADT van zalen van het reservatiesysteem
        :param plaatsen: het aantal plaatsen in de zaal
        :return: Het id van de nieuwe zaal wordt teruggegeven.

        preconditie: Het meegegeven aantal plaatsen is een positieve integer.

        postconditie: geen
        """
        zaal = Zaal(plaatsen, id_)
        self.zalen.tableInsert(self.zalen.tableLength(), zaal)
        return True

    # def meldAan(self, id):  # maker Khemin, tester Niels
    #     """
    #     Een functie die de gebruiker aanmeldt (door zijn status op True te zetten).
    #     :param id: Het id van de gebruiker die zich afmeldt; positieve integer
    #     :return: None
    #     post: De status van de gebruiker met het gegeven id is aangepast naar True.
    #     """
    #     self.gebruikers.tableRetrieve(id)[0].setStatus(True)
    #
    # def meldAf(self, id):  # maker Niels, tester Robin
    #     """
    #     Een functie die de gebruiker afmeldt (door zijn status op False te zetten).
    #     :param id: Het id van de gebruiker die zich afmeldt; positieve integer
    #     :return: None
    #     post: De status van de gebruiker met het gegeven id is aangepast naar False.
    #     """
    #     pass
    #
    # def film_available(self, filmid):  # maker Robin, tester Khemin
    #     """
    #     vraagt alle vertoningen met beschikbare plaatsen op, voor de gegeven film.
    #     :param filmid: Het id van de film waarvoor de evaluatie gemaakt moet worden. Dit is een positieve integer.
    #     :return: True als de film nog bekeken kan worden, anders False.
    #     post: self.vertoningen is niet van inhoud en/of lengte veranderd.
    #     """
    #     pass
