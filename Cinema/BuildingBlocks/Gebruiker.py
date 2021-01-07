from Cinema.BuildingBlocks import _Foundation


class Gebruiker(_Foundation):

    def __init__(self, id, voornaam, achternaam, email):
        """
        maakt de variabelen voornaam, achternaam, email
        :param voornaam: string (zie is_voornaam)
        :param achternaam: string (zie is_achternaam)
        :param email: string (geldige email)
        :param id: int

        :precondities: init moet opgeroepen zijn
        :postcondities: geen
        """
        self.id: int = id
        self.voornaam: str = voornaam
        self.achternaam: str = achternaam
        self.email: str = email
        self.logged_in: bool = False

    def getVoornaam(self) -> str:
        """
        :return: geef de voornaam terug
        """
        return self.voornaam

    def getAchternaam(self) -> str:
        """
        :return: geeft de achternaam terug
        """
        return self.achternaam

    def getEmail(self) -> str:
        """
        :return: geeft het email address terug
        """
        return self.email

    def isLoggedIn(self):
        """geeft terug of de user ingelogt is"""
        return self.logged_in

    def login(self):
        """logt de gebruiker in"""
        self.logged_in = True

    def logout(self):
        """logt de user uit"""
        self.logged_in = False
