"""Deze ADT stelt een vertoning voor.
Een vertoning wordt gedefineerd door een unieke id (zoeksleutel).
Verder heeft een vertoning nog een zaalnummer, een slot, een datum, een filmid
en een aantal vrije plaatsen.
"""


class Vertoning:

    def __init__(self, id=0, zaalnummer=0, slot="", datum="", filmid=0, aantal_vrij=0):
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
        self.id = id
        self.zaalnummer = zaalnummer
        self.slot = slot
        self.datum = datum
        self.filmid = filmid
        self.aantal_vrij = aantal_vrij
        self.playing = False

    @property
    def id(self):
        """
        Een functie die de waarde van id teruggeeft.

        preconditie: geen

        postconditie: De gebruiker is niet veranderd.
        """
        return self.id_

    @property
    def get_zaalnummer(self):
        """
        Een functie die de zaalnummer teruggeeft.

        preconditie: geen

        postconditie: De gebruiker is niet veranderd.
        """
        return self.zaalnummer

    @property
    def get_slot(self):
        """
        Een functie die de slot teruggeeft.

        preconditie: geen

        postconditie: De gebruiker is niet veranderd.
        """
        return self.slot

    @property
    def get_datum(self):
        """
        Een functie die de datum teruggeeft.

        preconditie: geen

        postconditie: De gebruiker is niet veranderd.
        """
        return self.datum

    @property
    def get_filmid(self):
        """
        Een functie die de filmid teruggeeft.

        preconditie: geen

        postconditie: De gebruiker is niet veranderd.
        """
        return self.filmid

    @property
    def get_aantal_vrij(self):
        """
        Een functie die de aantal_vrij teruggeeft.

        preconditie: geen

        postconditie: De gebruiker is niet veranderd.
        """
        return self.aantal_vrij


    def set_id(self, value):
        """
        Een functie die de id update naar de gegeven waarde.
        :param value: de nieuwe waarde van id

        preconditie: De gegeven value is een positieve integer.

        postconditie: De waarde van id is geüpdatet naar de gegeven value.
        """
        self.id = value


    def set_zaalnummer(self, value):
        """
        Een functie die de zaalnummer update naar de gegeven waarde.
        :param value: de nieuwe zaalnummer

        preconditie: De gegeven value is een positieve integer.

        postconditie: De waarde van id is geüpdatet naar de gegeven value.
        """
        self.zaalnummer = value


    def set_slot(self, value):
        """
        Een functie die de slot update naar de gegeven waarde.
        :param value: het nieuwe slot

        preconditie: De gegeven value is een string.

        postconditie: De slot is geüpdatet naar de gegeven value.
        """
        self.slot = value


    def set_datum(self, value):
        """
        Een functie die de datum update naar de gegeven waarde.
        :param value: de nieuwe datum

        preconditie: De gegeven value is een string.

        postconditie: De datum is geüpdatet naar de gegeven value.
        """
        self.datum = value


    def set_filmid(self, value):
        """
        Een functie die de filmid update naar de gegeven waarde.
        :param value: de nieuwe filmid

        preconditie: De gegeven value is een positieve integer.

        postconditie: De filmid is geüpdatet naar de gegeven value.
        """
        self.filmid = value


    def set_aantal_vrij(self, value):
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
        pass


    def stop(self):
        """
        Een methode die een vertoning stopt door het playing attribuut op False te zetten.
        :return: Als de vertoning niet aan het spelen is wordt er False teruggegeven. Al de stop succesvol was wordt er True teruggegeven.

        preconditie: geen

        postconditie: geen
        """
        pass
