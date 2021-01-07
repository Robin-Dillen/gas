from Cinema.BuildingBlocks import Gebruiker
from Cinema.DataStructures import LinkedChainTable
from typing import Optional


class GebruikerSysteem:
    def __init__(self):
        self.gebruikers = LinkedChainTable()
        self.logged_in_user: Optional[Gebruiker] = None

    def create_account(self, id: int, voornaam: str, achternaam: str, email: str) -> bool:
        """
        Voeg een user toe aan de dict gebruikers met id = Gebruiker.get_id() voor toevoeging element,
        als Gebruiker.get_id() None teruggeeft dan is id = len(self.gebruikers) (voor toevoeging object)
        :param voornaam: string (check voor juiste format)
        :param achternaam: string (check voor juiste format)
        :param email: string (check voor juiste format)
        :return: succes als het gelukt is (bool)

        :precondities: geen
        :postcondities: id als het gelukt is anders False
        """
        gebruiker = Gebruiker(id, voornaam, achternaam, email)
        self.gebruikers.tableInsert(self.gebruikers.tableLength(), gebruiker)
        print(f'User {voornaam} created!')
        return True

    def delete_account(self, id):
        """
        vervangt het object op plaats id in gebruikers door None, roept Gebruiker.add_unused_id(id) op als id != len(gebruikers)
        :param id: 0 <= id:int
        :return: Succes

        :precondities: de gebruiker moet ingelogt zijn
        :postcondities: gebruikers bevat een element minder
        """
        pass

    def login(self, id: int):
        """
        logged de gebruiker in
        :param email: string (juiste format)
        :param password: (juiste format)
        :return: Succes

        :precondities: de gebruiker moet bestaan
        :postcondities: Succes als de gebruiker is ingelogt, anders False
        """
        user, succes = self.gebruikers.tableRetrieve(id)
        if not succes:
            return False

        user.login()
        print(f"{user.getVoornaam() + ' ' + user.getAchternaam()} is ingelogt")
        return True

    def logout(self, id: int):
        """
        zet logged_in_user = None
        :return: Succes

        :preconditie: de gebruiker moet ingelogt zijn
        :postconditie: succes is True als de gebruiker is uitgelogt, anders False(als de gebruiker bv niet ingelogt was)
        """
        user, succes = self.gebruikers.tableRetrieve(id)
        if not succes:
            return False
        user.logout()
        print(f"{user.voornaam + ' ' + user.getAchternaam()} heeft zich uitgelogt!")