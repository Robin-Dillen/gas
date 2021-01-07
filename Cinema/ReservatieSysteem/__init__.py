from Cinema.BuildingBlocks import Reservatie
from Cinema.DataStructures import Queue

from Cinema.ReservatieSysteem.GebruikerSysteem import GebruikerSysteem
from Cinema.ReservatieSysteem.VertoningSysteem import VertoningSysteem


import datetime


class ReservatieSysteem(GebruikerSysteem, VertoningSysteem):
    def __init__(self):
        # super().__init__() doesnt work
        GebruikerSysteem.__init__(self)
        VertoningSysteem.__init__(self)

        self.reservaties = Queue()

    def place_reservation(self, datetime_, user_id, vertoning_id, aantal_plaatsen):
        """
        maak een reservatie, roep Gebruiker.add_reservation(reservatie) op
        :param vertoning: vertoning object
        :param aantal_plaatsen:0 <= int aantal_plaatsen
        :return: Succes

        :preconditie: de gebruiker moet ingelogt zijn, de gebruiker mag nog geen reservatie op die moment hebben, de vertoning mag niet vol zijn
        :postconditie: succes is True als de reservatie is toegvoegt en alles kon correct word geüpdate, anders False(als de gebruiker bv niet ingelogt was)
        """
        vertoning, succes = self.vertoningen.tableRetrieve(vertoning_id)
        if not succes or vertoning.getVrijePlaatsen() - aantal_plaatsen < 0:
            return False
        self.reservaties.enqueue(Reservatie(datetime_, user_id, vertoning_id, aantal_plaatsen))
        vertoning.updateReservaties(aantal_plaatsen)
        print(f"De reservatie is aangemaakt!")
        return True

    def log(self, time: str):
        with open("log.html", "w") as f:
            buffer = "<html><head><style>table {border-collapse: collapse;}table, td, th {border: 1px solid #000000;}</style></head><body>"
            buffer += f"<h1>Log op {time}</h1>"
            f.write(buffer)
            vertoningen = []
            self.vertoningen.traverseTable(vertoningen.append)
            for vertoning in vertoningen:
                pass