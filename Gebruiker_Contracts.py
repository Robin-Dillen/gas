"""Deze ADT stelt een gebruiker voor.
Een gebruiker wordt gedefineerd door een unieke id (zoeksleutel).
Verder heeft een gebruiker nog een voornaam, een achternaam en een e-mailadres."""


class Gebruiker:
    def __init__(self, id, voornaam, achternaam, email):
        """
        Initialiseert een nieuwe gebruiker met de opgegeven id, voornaam, achternaam en e-mailadres.
        :param id: de unieke id van de gebruiker, is een positieve integer.
        :param voornaam: de voornaam van de gebruiker, is een string.
        :param achternaam: de achternaam van de gebruiker, is een string.
        :param email: het e-mailadres van de gebruiker, is een string
        """
        self.id_ = id
        self.voornaam_ = voornaam
        self.achternaam_ = achternaam
        self.email_ = email
        self.status_ = False

    def getId(self):
        """
        :return: id
        post: De gebruiker is niet veranderd.
        """
        return self.id_

    def setId(self, id_):
        """
        Een functie die de id update naar de gegeven waarde.
        :param id: is een positieve integer
        :return: None
        post: De waarde van id is geüpdatet naar de gegeven value.
        """
        self.id_ = id_

    def getVoornaam(self):
        """
        :return: voornaam
        post: De gebruiker is niet veranderd.
        """
        return self.voornaam_

    def setVoornaam(self, voornaam):
        """
        Een functie die de voornaam update naar de gegeven waarde.
        :param voornaam: is een string
        :return: None
        post: De waarde van voornaam is geüpdatet naar de gegeven value.
        """
        self.voornaam_ = voornaam

    def getAchternaam(self):
        """
        :return: achternaam
        post: De gebruiker is niet veranderd.
        """
        return self.achternaam_

    def setAchternaam(self, achternaam):
        """
        Een functie die de achternaam update naar de gegeven waarde.
        :param achternaam: is een string
        :return: None
        post: De waarde van achternaam is geüpdatet naar de gegeven value.
        """
        self.achternaam_ = achternaam

    def getEmail(self):
        """
        :return: email
        post: De gebruiker is niet veranderd.
        """
        return self.email_

    def setEmail(self, email):
        """
        Een functie die de email update naar de gegeven waarde.
        :param email: is een string
        :return: None
        post: De waarde van email is geüpdatet naar de gegeven value.
        """
        self.email_ = email

    def getStatus(self):
        """
        :return: status
        post: De gebruiker is niet veranderd.
        """
        return self.status_

    def setStatus(self, status):
        """
        Een functie die de status update naar de gegeven waarde.
        :param status: is een bool
        :return: None
        post: De waarde van status is geüpdatet naar de gegeven value.
        """
        self.status_ = status

