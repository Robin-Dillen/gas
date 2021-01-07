from Cinema.BuildingBlocks import Vertoning
from Cinema.DataStructures import BSTTable
from typing import Tuple, Optional
from Cinema.Types import _BuildingBlock

from Cinema.ReservatieSysteem.ZaalSysteem import ZaalSysteem
from Cinema.ReservatieSysteem.FilmSysteem import FilmSysteem


class VertoningSysteem(ZaalSysteem, FilmSysteem):
    def __init__(self):
        FilmSysteem.__init__(self)
        ZaalSysteem.__init__(self)
        self.vertoningen = BSTTable()

    def retrieve_vertoning(self, vertoning_id) -> Tuple[Optional[_BuildingBlock], bool]:
        """
        geef de vertoning met gegeven id terug
        :param film_id: 0 <= int id
        :return: vertoning

        :preconditie: geen
        :postconditie: geeft de vertoning met gegeven id terug
        """
        return self.vertoningen.tableRetrieve(vertoning_id)

    def add_vertoning(self, id, zaalnummer, tijdsslot, datum, film_id):
        """
        voegt een vertoning toe aan vertoningen
        :param zaalnummer: zaalnummer
        :param tijdsslot: timedelte object
        :param datum: datetime object
        :param film_id: id
        :return: id van de vertoning

        :preconditie: geen
        :postconditie: er zit een vertoning meer in vertoningen
        """
        vertoning = Vertoning(id, zaalnummer, tijdsslot, datum, film_id, 100)
        self.vertoningen.tableInsert(vertoning)

        print(f"de vertoning {vertoning.getSearchKey()} is toegevoegt!")
        return vertoning.getSearchKey()

    def remove_vertoning(self, vertoning_id: int) -> bool:
        """
        verwijdert een vertoning uit vertoningen
        :param vertoning_id: id
        :return: Succes

        :preconditie:
        :postconditie: er zit een vertoning meer in vertoningen
        """
        return self.vertoningen.tableDelete(vertoning_id)

    def update_vertoning(self, vertoning_id: int, aantal_plaatsen: int):
        """
        update het aantal plaatsen dat nodig is om de vertoning te starten
        :param vertoning_id: selecteert welke vertoning wordt geüpdate
        :param aantal_plaatsen: int
        :return: return true als de vertoning kan beginnen anders False
        """
        vertoning, succes = self.vertoningen.tableRetrieve(vertoning_id)
        if not succes:
            return False

        vertoning.addAantalMensenZaal(vertoning.getVrijePlaatsen() - aantal_plaatsen)
