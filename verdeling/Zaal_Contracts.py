"""Deze ADT stelt een zaal voor.
Een zaal wordt gedefineerd door een nummer (zoeksleutel).
Verder heeft een zaal nog een aantal plaatsen."""


class Zaal:
    def __init__(self, zaalnummer, plaatsen):
        """
        Initialiseert een nieuwe film met de opgegeven zaalnummer en plaatsen.
        :param zaalnummer: het zaalnummer van de zaal, is een positieve integer
        :param plaatsen: het aantal plaatsen in de zaal , is een strict positieve integer.
        """
        self.zaalnummer_ = zaalnummer
        self.plaatsen_ = plaatsen

    def getId(self):
        """
        Een functie die het zaalnummer teruggeeft.
        :return: zaalnummer
        post: De film is niet veranderd.
        """
        return self.zaalnummer_

    def setId(self, zaalnummer):
        """
        Een functie die het zaalnummer update naar de gegeven waarde.
        :param zaalnummer: het nieuwe zaalnummer, is een positieve integer.
        :return: None
        post: De waarde van zaalnummer is geüpdatet naar de gegeven value.
        """
        self.zaalnummer_ = zaalnummer

    def getPlaatsen(self):
        """
        Een functie die het plaatsen teruggeeft.
        :return: plaatsen
        post: De film is niet veranderd.
        """
        return self.plaatsen_

    def setPlaatsen(self, plaatsen):
        """
        Een functie die het plaatsen update naar de gegeven waarde.
        :param plaatsen: het nieuwe plaatsen, is een positieve integer.
        :return: None
        post: De waarde van plaatsen is geüpdatet naar de gegeven value.
        """
        self.plaatsen_ = plaatsen

