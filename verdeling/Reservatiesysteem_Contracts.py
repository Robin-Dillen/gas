"""
Deze ADT stelt het beheer van het volledige reservatiesysteem voor.
Het bevat verschillende functies om de kleiner ADT's (Film, Gebruiker,
Reservatie, Vertoning, Zaal) samen te brengen in een groter geheel.
"""
import datetime

from verdeling.Film_Contracts import Film
from verdeling.Gebruiker_Contracts import Gebruiker
from verdeling.Reservatie_Contracts import Reservatie
from verdeling.Vertoning_Contracts import Vertoning
from verdeling.Zaal_Contracts import Zaal
from verdeling.Clock import clock

user = input("Khemin, Niels of Robin?: ")
user = user.lower()

if user.lower() == "robin":
    user = "Robin"
    from verdeling.Robin.DataStructures import BSTTable, LinkedChainTable, Queue

elif user.lower() == "khemin":
    user = "Khemin"
    from verdeling.Khemin.Datastructures.BST import *
    from verdeling.Khemin.Datastructures.LinkedChain import *
    from verdeling.Khemin.Datastructures.Queue import *

else:
    user = "Niels"
    from verdeling.Niels.Datastructures.BST import *
    from verdeling.Niels.Datastructures.LinkedChain import *
    from verdeling.Niels.Datastructures.Queue import *


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

    def retrieveVertoningen(self, id) -> (object, bool):  # maker Khemin, tester Niels
        """
        Een functie die uit een datastructuur van objecten het object haalt met het opgegeven id.
        Het object wordt teruggegeven indien het gevonden wordt in het ADT. Als het niet in de ADT zit wordt er None teruggegeven.
        :param id: id van het object, is een positieve integer.
        :return:  Object, succes
        post: De gegeven lst is niet van inhoud en/of lengte veranderd.
        """
        return self.vertoningen.tableRetrieve(id)

    def maakAccount(self, id, voornaam, achternaam, email) -> bool:  # maker Niels, tester Robin
        """
        Een functie die voor de gegeven voornaam,achternaam en e-mailadres een
        nieuw gebruiker aanmaakt en deze toevoegd aan het ADT van gebruiker van het reservatiesysteem.
        :param voornaam: de voornaam van de nieuwe gebruiker, is een string.
        :param achternaam: de achternaam van de nieuwe gebruiker, is een string.
        :param email: het e-mailadres van de nieuwe gebruiker, is een string.
        :return: Geeft True terug als het account succesvol is toegevoegd
        """
        gebruiker = Gebruiker(id, voornaam, achternaam, email)
        self.gebruikers.tableInsert(self.gebruikers.tableLength() + 1, gebruiker)
        return True

    def addFilm(self, id, titel, rating) -> bool:  # maker Robin, tester Khemin
        """
        Een functie die voor de gegeven titel en rating een
        nieuw film aanmaakt en deze toevoegd aan het ADT van films van het reservatiesysteem.
        :param titel: de titel van de film, is een string.
        :param rating: de rating van de film, is een float tussen 0-10.
        :return: Geeft True terug als de film succesvol is toegevoegd
        """
        if self.films.tableSearch(id):
            print(f"\033[1;31;49mThe id: {id}, is already in use! The move {titel} has NOT been created!\033[0m")
            return False
        film = Film(id, titel, rating)
        self.films.tableInsert(self.films.tableLength() + 1, film)
        print(f"The movie {titel} has been created!")
        return True

    def addReservatie(self, timestamp, userid, vertoningid, plaatsen) -> bool:  # maker Khemin, tester Niels
        """
        Een functie die voor de gegeven userid, timestamp, vertoninging en plaatsen een nieuw reservatie aanmaakt en deze toevoegd aan het ADT van reservaties van het reservatiesysteem.
        :param userid : de userid van de gebruiker die de reservatie aangemaakt heeft.
        :param timestamp : Het tijdstip waarop de reserveerde vertoning gespeeld wordt.
        :param vertoningid : het id van de vertoning die gereserveerd werd.
        :param plaatsen : het aantal plaatsen dat gereserveerd wordt
        :return: Geeft True terug als de reservatie succesvol is toegevoegd

        preconditie:
            De meegegeven userid is een positieve integer.
            De meegegeven timestamp is een tuple met twee strings als elementen. De eerste string geeft het tijdstip van reservatie weer, de tweede geeft de reservatiedatum weer.
            De meegegeven vertoningid is een positieve integer.
            De meegegeven plaatsen is een positieve integer.

        postconditie: geen
        """
        vertoning, succes = self.retrieveVertoningen(vertoningid)
        vertoning: Vertoning
        if not succes or vertoning.getAantalVrij() <= plaatsen:  # checkt of er de vertoning is geretrieved en of er genoeg plaatsen beschikbaar zijn
            return False

        aantal_vrij = vertoning.getAantalVrij() - plaatsen  # het nieuwe aantal vrije plaatsen
        vertoning.setAantalVrij(aantal_vrij)
        self.reservaties.enqueue(Reservatie(userid, timestamp, vertoningid, plaatsen))

    def addVertoning(self, id, zaalnummer, slot, datum, filmid, aantal_vrij) -> bool:  # maker Niels, tester Robin
        """
        Een functie die voor de gegeven zaalnummer, slot, datum, filmid en aantal_vrij een
        nieuw vertoning aanmaakt en deze toevoegd aan het ADT van vertoningen van het reservatiesysteem.
        :param zaalnummer: het zaalnummer van de zaal waar de vertoning gespeeld wordt., is een positieve integer.
        :param slot: Het tijdstip waarop de vertoning gespeeld wordt, is een datetime.timedelta.
        :param datum: het datum waarop de vertoning gespeeld wordt, is een datetime.datime object.
        :param filmid: het id van de film die gespeeld zal worden tijdens de vertonging, is een positieve integer.
        :param aantal_vrij: het aantal vrije plaatsen in de zaal van de vertoning, is een positieve integer.
        :return: Geeft True terug als de vertoning succesvol is toegevoegd
        """
        if not self.zalen.tableSearch(zaalnummer):
            raise Exception("Zaal bestaat niet!")
        vertoning = Vertoning(id, zaalnummer, slot, datum, filmid, aantal_vrij)
        self.vertoningen.tableInsert(vertoning.getId() + 1, vertoning)
        film = self.films.tableSearch(filmid)
        if film:
            film.addVertoning(vertoning)
        return True

    def updateTicketten(self, vertoning_id, ticketten) -> bool:
        """
        Als mensen binnenkomen bij de vertoning worden de ticketten afgetrokken
        :param vertoning_id: id van de vertoning
        :param ticketten: aantal mensen dat binnenkomt
        :return: true als succes
        """
        vertoning: Vertoning
        vertoning, succes = self.vertoningen.tableRetrieve(vertoning_id)
        if succes:
            vertoning.setAantalMensenBinnen(vertoning.getAantalMensenBinnen() + ticketten)
            zaal: Zaal
            zaal, succes = self.zalen.tableRetrieve(vertoning.getZaalnummer())
            if succes and vertoning.getAantalMensenBinnen() + vertoning.getAantalVrij() == zaal.getPlaatsen():
                vertoning.start()
            return True
        return False

    def addZaal(self, id_, plaatsen) -> bool:  # maker Robin, tester Khemin
        """
        Een functie die voor de gegeven titel en rating een nieuwe zaal aanmaakt en deze toevoegd aan het ADT van zalen van het reservatiesysteem
        :param plaatsen: het aantal plaatsen in de zaal
        :return: Geeft True terug als de zaal succesvol is toegevoegd

        preconditie: Het meegegeven aantal plaatsen is een positieve integer.

        postconditie: geen
        """
        zaal = Zaal(id_, plaatsen)
        self.zalen.tableInsert(self.zalen.tableLength() + 1, zaal)
        return True

    def makeLog(self, time):
        """
        maakt een html file aan met alle films, hun speeltijden en het aantal reservaties/
        aantal mensen waarop gewacht word/ aantal mensen dat in de zaal was
        :return: None
        """
        BOF = """
        <html>
	<head>
	<style>
		table {
		    border-collapse: collapse;
		}

		table, td, th {
		    border: 1px solid #000000;
		}
	</style>
</head>
	<body>
		<h1>Log op """ + time + """, met de ADTS van: """ + user + """</h1>
		<table>
			<thead>
				<td>Datum</td>
				<td>Film</td>
				<td>14:30</td>
				<td>17:00</td>
				<td>20:00</td>
				<td>22:30</td>
			</thead>
			<tbody>
        """
        body = ""
        EOF = "</tbody></table></body></html>"
        with open("log.html", "w") as f:
            f.write(BOF)
            films = []
            self.films.traverseTable(films.append)  # zet alle films in films
            for film in films:
                titel = film.getTitel()
                for day in film.getVertoningen():
                    body += self.__generateTable(titel, day)

            f.write(body)
            f.write(EOF)

    def __generateTable(self, titel, day):
        slots = [datetime.time(14, 30), datetime.time(17, 0), datetime.time(20, 0), datetime.time(22, 30)]
        slot_pos = 0
        buffer = f"""
                    <tr>
                        <td>{day[0].date()}</td>
                        <td>{titel}</td>
                        """
        for vertoning in day[1]:
            while vertoning[0] != slots[slot_pos]:
                buffer += f"<td></td>"
                slot_pos += 1

            zaal, succes = self.zalen.tableRetrieve(vertoning[1].getZaalnummer())
            if not succes:
                raise Exception("Zaal niet gevonden!")

            if vertoning[1].isStarted() or vertoning[1].getAantalVrij() == zaal.getPlaatsen():
                buffer += f"<td>F:{vertoning[1].getAantalMensenBinnen()}</td>"

            elif vertoning[1].isWaiting():
                buffer += f"<td>W:{zaal.getPlaatsen() - (vertoning[1].getAantalMensenBinnen() + vertoning[1].getAantalVrij())}</td>"

            else:
                buffer += f"<td>G:{zaal.getPlaatsen() - vertoning[1].getAantalVrij()}</td>"

            slot_pos += 1

        for _ in range(slot_pos, 4):
            buffer += f"<td></td>"

        buffer += "</tr>"
        return buffer



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
