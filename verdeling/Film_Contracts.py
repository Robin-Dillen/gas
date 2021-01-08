"""Deze ADT stelt een film voor.
Een film wordt gedefineerd door een unieke id (zoeksleutel).
Verder heeft een film nog een titel en een rating."""


class Film:
    def __init__(self, id_=0, titel="", rating=0.0):
        """
        Initialiseert een nieuwe film met de opgegeven id, titel en rating.

        :param id: het id van de film, is een positieve integer
        :param titel: de titel van de film, is een string.
        :param rating: de rating van de film, is een float tussen 0 en 10
        """
        self.id_ = id_
        self.titel_ = titel
        self.rating_ = rating

    def getId(self):
        """
        :return: id
        post: De film is niet veranderd.
        """
        return self.id_

    def setId(self, id):
        """
        Een functie die de id update naar de gegeven waarde.
        :param id: de nieuwe waarde van id, is een positieve integer
        :return: None
        pre: geen
        post: De waarde van id is geüpdatet naar de gegeven value.
        """
        self.id_ = id

    def getTitel(self):
        """
        :return: titel
        post: De film is niet veranderd.
        """
        return self.titel_

    def setTitel(self, titel):
        """
        Een functie die de titel update naar de gegeven waarde.
        :param titel: de nieuwe waarde van titel; string
        :return: None
        pre: geen
        post: De waarde van titel is geüpdatet naar de gegeven value.
        """
        self.titel_ = titel

    def getRating(self):
        """
        :return: rating
        post: De film is niet veranderd.
        """
        return self.rating_

    def setRating(self, rating):
        """
        Een functie die de rating update naar de gegeven waarde.
        :param rating: de nieuwe waarde van rating; float tussen 0-10
        :return: None
        pre: geen
        post: De waarde van rating is geüpdatet naar de gegeven value.
        """
        self.rating_ = rating
