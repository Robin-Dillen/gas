from Cinema.BuildingBlocks import Zaal
from Cinema.DataStructures import LinkedChainTable


class ZaalSysteem:
    def __init__(self):
        self.zalen = LinkedChainTable()

    def add_zaal(self, id: int, capacity: int) -> bool:
        """
        Voeg een zaal toe
        :param id: id van de zaal, int
        :param capacity: strict positieve int
        :return: succes
        :preconditie: geen
        :postconditie: zalen bevat een element meer
        """
        zaal = Zaal(capacity, id)
        self.zalen.tableInsert(self.zalen.tableLength(), zaal)
        return True

    def delete_movie(self, id):
        """
        vervang het object op de plaats id in films door None, roept Film.add_unused_id(id) op als id != len(films) - 1
        :param id: 0 <= int id < len(films)
        :return: Succes

        :preconditie: geen
        :postconditie: Succes als het gelukt is anders False, films bevat een object minder
        """
        pass