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

# Keuze ADT's
user = input("Khemin, Niels of Robin?: ")
user = user.lower()

if user.lower() == "robin":
    user = "Robin"
    from verdeling.Robin.DataStructures import BSTTable, LinkedChainTable, Queue, RedBlackTreeTable

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
    from verdeling.Niels.Datastructures.TwoThreeTree import *


class Reservatiesysteem:
    def __init__(self, films=LinkedChainTable(), gebruikers=LinkedChainTable(),
                 reservaties=Queue(), vertoningen=RedBlackTreeTable(),
                 zalen=LinkedChainTable()):

        self.films = films
        self.gebruikers = gebruikers
        self.reservaties = reservaties
        self.vertoningen = vertoningen
        self.zalen = zalen
        self.tijd = 0

    def retrieveVertoningen(self, id) -> (object, bool):
        """
        Een functie die uit een datastructuur van objecten het object haalt met het opgegeven id.
        Het object wordt teruggegeven indien het gevonden wordt in het ADT. Als het niet in de ADT zit wordt er None teruggegeven.
        :param id: id van het object, is een positieve integer.
        :return:  Object, succes
        post: De gegeven lst is niet van inhoud en/of lengte veranderd.
        """
        return self.vertoningen.tableRetrieve(id)  # Kijkt na of de vertoning met gegeven id bestaat

    def maakAccount(self, id, voornaam, achternaam, email) -> bool:
        """
        Een functie die voor de gegeven voornaam,achternaam en e-mailadres een
        nieuw gebruiker aanmaakt en deze toevoegd aan het ADT van gebruiker van het reservatiesysteem.
        :param voornaam: de voornaam van de nieuwe gebruiker, is een string.
        :param achternaam: de achternaam van de nieuwe gebruiker, is een string.
        :param email: het e-mailadres van de nieuwe gebruiker, is een string.
        :return: Geeft True terug als het account succesvol is toegevoegd
        """
        if self.gebruikers.tableRetrieve(id)[1]:
            print(f"\033[1;31;49mThe id: {id}, is already in use! user not created!\033[0m")
            return False
        gebruiker = Gebruiker(id, voornaam, achternaam, email)
        self.gebruikers.tableInsert(self.gebruikers.tableLength() + 1, gebruiker)
        return True

    def addFilm(self, id, titel, rating) -> bool:
        """
        Een functie die voor de gegeven titel en rating een
        nieuw film aanmaakt en deze toevoegd aan het ADT van films van het reservatiesysteem.
        :param titel: de titel van de film, is een string.
        :param rating: de rating van de film, is een float tussen 0-10.
        :return: Geeft True terug als de film succesvol is toegevoegd
        """
        if self.films.tableRetrieve(id)[1]:  # Kijkt na of film-id al bestaat
            print(f"\033[1;31;49mThe id: {id}, is already in use! The move {titel} has NOT been created!\033[0m")
            return False
        film = Film(id, titel, rating)  # Nieuwe film aanmaken
        self.films.tableInsert(self.films.tableLength() + 1, film)  # Film toevoegen aan ADT van films
        print(f"The movie {titel} has been created!")
        return True

    def addReservatie(self, timestamp, userid, vertoningid, plaatsen) -> bool:
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

        vertoning, succes = self.retrieveVertoningen(vertoningid)  # vertoning is 1ste element van de tuple, succes is het 2de element
        vertoning: Vertoning
        if not succes or vertoning.getAantalVrij() <= plaatsen:  # checkt of er de vertoning is geretrieved en of er genoeg plaatsen beschikbaar zijn
            return False
        aantal_vrij = vertoning.getAantalVrij() - plaatsen  # het nieuwe aantal vrije plaatsen
        vertoning.setAantalVrij(aantal_vrij)
        self.reservaties.enqueue(Reservatie(userid, timestamp, vertoningid, plaatsen))  # voegt de reservatie toe aan de ADT van reservaties

    def addVertoning(self, id, zaalnummer, slot, datum, filmid, aantal_vrij) -> bool:
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
        if not self.zalen.tableRetrieve(zaalnummer)[1]: # Kijkt na of de gegeven zaal met zaalnummer bestaat
            raise Exception("Zaal bestaat niet!")
        vertoning = Vertoning(id, zaalnummer, slot, datum, filmid, aantal_vrij) # maakt een nieuwe vertoning aan
        self.vertoningen.tableInsert(self.vertoningen.tableLength() + 1, vertoning) # voegt de vertoning toe aan de ADT van vertoningen
        film, succes = self.films.tableRetrieve(filmid) # film is 1ste element van de tuple, succes is het 2de element
        if succes:  # Kijkt na of de film is gevonden
            film.addVertoning(vertoning)    # Voegt de vertoning toe aan de film
        return True

    def updateTicketten(self, vertoning_id, ticketten) -> bool:
        """
        Als mensen binnenkomen bij de vertoning worden de ticketten afgetrokken
        :param vertoning_id: id van de vertoning
        :param ticketten: aantal mensen dat binnenkomt
        :return: true als succes
        """
        vertoning: Vertoning
        vertoning, succes = self.vertoningen.tableRetrieve(vertoning_id)    # vertoning is 1ste element van de tuple, succes is het 2de element
        if succes:  # kijkt na of de vertoning bestaat
            vertoning.setAantalMensenBinnen(vertoning.getAantalMensenBinnen() + ticketten)  # past het aantal personen aan dat in de zaal zit
            zaal: Zaal
            zaal, succes = self.zalen.tableRetrieve(vertoning.getZaalnummer())  # zaal is 1ste element van de tuple, succes is het 2de element
            if succes and vertoning.getAantalMensenBinnen() + vertoning.getAantalVrij() == zaal.getPlaatsen(): # kijkt na of de zaal bestaat, kijkt na of alle mensen binnen zijn
                vertoning.start()   # start de vertoning
            return True
        return False

    def addZaal(self, id_, plaatsen) -> bool:
        """
        Een functie die voor de gegeven titel en rating een nieuwe zaal aanmaakt en deze toevoegd aan het ADT van zalen van het reservatiesysteem
        :param plaatsen: het aantal plaatsen in de zaal
        :return: Geeft True terug als de zaal succesvol is toegevoegd

        preconditie: Het meegegeven aantal plaatsen is een positieve integer.

        postconditie: geen
        """
        zaal = Zaal(id_, plaatsen)  # maakt een nieuwe zaal aan
        self.zalen.tableInsert(self.zalen.tableLength() + 1, zaal)  # voegt de zaal toe aan de ADT van zalen
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
        with open("log.html", "w") as f:    # opent het output bestand om te schrijven
            f.write(BOF)    # schrijft BOF (formaat en standaardslots) in de output file
            films = []      # nieuwe lijst voor films
            self.films.traverseTable(films.append)  # zet alle films in films
            for film in films:  # loopt over films
                titel = film.getTitel() # krijg de titel van de film
                for day in film.getVertoningen():   # loopt over elke dag van vertoningen van deze film
                    body += self.__generateTable(titel, day)    # voegt een nieuwe rij toe voor elke dag dat deze film wordt afgespeeld en voegt dit toe aan body
            f.write(body)   # schrijft de body in het output bestand
            f.write(EOF)    # schrijft EOF (einde file) in het output bestand

    def __generateTable(self, titel, day):
        slots = [datetime.time(14, 30), datetime.time(17, 0), datetime.time(20, 0), datetime.time(22, 30)]  # standaard slots
        slot_pos = 0    # index slot_pos
        buffer = f"""
                    <tr>
                        <td>{day[0].date()}</td>
                        <td>{titel}</td>
                        """
        for vertoning in day[1]:    # loopt over de vertoningen van de dag
            while vertoning[0] != slots[slot_pos]:  # Zolang er geen vertoning is op dit slot, wordt <td></td> bij de buffer toegevoegd
                buffer += f"<td></td>"  # geen vertoning
                slot_pos += 1   # naar volgende positie gaan

            zaal, succes = self.zalen.tableRetrieve(vertoning[1].getZaalnummer())   # zaal is 1ste element van de tuple, succes is het 2de element
            if not succes:  # kijkt na of zaal bestaat
                raise Exception("Zaal niet gevonden!")

            if vertoning[1].isStarted() or vertoning[1].getAantalVrij() == zaal.getPlaatsen():  # als de film gestart is
                buffer += f"<td>F:{vertoning[1].getAantalMensenBinnen()}</td>"  # voeg "F: aantal mensen in zaal" toe aan buffer

            elif vertoning[1].isWaiting():  # als er gewacht moet worden op personen
                buffer += f"<td>W:{zaal.getPlaatsen() - (vertoning[1].getAantalMensenBinnen() + vertoning[1].getAantalVrij())}</td>"   # voeg "W: aantal mensen waarop wachten" toe aan buffer

            else:
                buffer += f"<td>G:{zaal.getPlaatsen() - vertoning[1].getAantalVrij()}</td>" # voeg "G: aantal verkochte tickets" toe aan buffer

            slot_pos += 1   # ga naar volgende slot

        for _ in range(slot_pos, 4):    # voeg aan volgende slots <td></td> toe
            buffer += f"<td></td>"

        buffer += "</tr>"
        return buffer
