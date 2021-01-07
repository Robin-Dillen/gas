from Cinema.BuildingBlocks import Film
from Cinema.DataStructures import LinkedChainTable


class FilmSysteem:
    def __init__(self):
        self.films = LinkedChainTable()

    def add_movie(self, id, titel, rating) -> bool:
        """
        Voeg een film toe aan de dict films met id = Film.get_id() voor toevoeging element,
        als Film.get_id() None teruggeeft dan is id = len(self.films) (voor toevoeging object)
        :param titel: string (uniek)
        :param rating: 0 <= float(rating) <= 10
        :return: succes als het gelukt is, anders false

        :preconditie: geen
        :postconditie: films bevat een element meer
        """
        film = Film(id, titel, rating)
        self.films.tableInsert(self.films.tableLength(), film)
        print(f"The movie {titel} has been created!")
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