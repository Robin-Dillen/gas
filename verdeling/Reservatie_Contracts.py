"""
Deze ADT stelt een reservatie voor.
Een reservatie wordt gedefineerd door een unieke id (zoeksleutel).
Verder heeft een gebruiker nog een userid, een timestamp, een vertoningid
en een aantal plaatsen.
"""


class Reservatie:

    def __init__(self, id_=0, userid=0, timestamp=("",""), vertoningid=0, plaatsen=0):
        """
        Initialiseert een nieuwe reservatie met de opgegeven id, userid, timestamp, vertoningid
        en plaatsen.

        :param id: de unieke id van de reservatie, is een positieve integer.
        :param userid: de userid van de gebruiker die de reservatie aangemaakt heeft. Dit is een positieve integer.
        :param timestamp: Het tijdstip waarop de reserveerde vertoning gespeeld wordt. Dit is een tuple met twee
                            strings als elementen. De eerste string geeft het tijdstip van reservatie weer, de tweede
                                geeft de reservatiedatum weer.
        :param vertoningid: het id van de vertoning die gereserveerd werd. Dit is een positieve integer
        :param plaatsen: het aantal plaatsen dat gereserveerd wordt. Dit is een positieve integer.
        """
        self.id_ = id_
        self.userid_ = userid
        self.timestamp_ = timestamp
        self.vertoningid_ = vertoningid
        self.plaatsen_ = plaatsen

    @property
    def id(self):
        """
        :return: De waarde van id
        post: De gebruiker is niet veranderd.
        """
        return self.id

    @id.setter
    def id(self, id_):
        """
        Een functie die de id update naar de gegeven waarde.
        :param id: De nieuwe waarde van id; positieve integer
        :return: None
        post: De waarde van id is geüpdatet naar de gegeven value.
        """
        self.id_ = id_

    @property
    def userid(self):
        """
        :return: De waarde van userid
        post: De gebruiker is niet veranderd.
        """
        return self.userid

    @userid.setter
    def userid(self, userid):
        """
        Een functie die de userid update naar de gegeven waarde.
        :param userid: De nieuwe waarde van userid; positieve integer
        :return: None
        post: De waarde van userid is geüpdatet naar de gegeven value.
        """
        self.userid_ = userid

    @property
    def timestamp(self):
        """
        :return: De waarde van timestamp
        post: De gebruiker is niet veranderd.
        """
        return self.timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Een functie die de timestamp update naar de gegeven waarde.
        :param timestamp: De nieuwe waarde van timestamp, een tuple met 2 string elementen.
        :return: None
        post: De waarde van timestamp is geüpdatet naar de gegeven value.
        """
        self.timestamp_ = timestamp

    @property
    def vertoningsid(self):
        """
        :return: De waarde van vertoningsid
        post: De gebruiker is niet veranderd.
        """
        return self.vertoningsid

    @vertoningsid.setter
    def vertoningsid(self, vertoningsid):
        """
        Een functie die de vertoningsid update naar de gegeven waarde.
        :param vertoningsid: De nieuwe waarde van vertoningsid; positieve integer
        :return: None
        post: De waarde van vertoningsid is geüpdatet naar de gegeven value.
        """
        self.vertoningsid_ = vertoningsid

    @property
    def plaatsen(self):
        """
        :return: De waarde van plaatsen
        post: De gebruiker is niet veranderd.
        """
        return self.plaatsen

    @plaatsen.setter
    def plaatsen(self, plaatsen):
        """
        Een functie die de plaatsen update naar de gegeven waarde.
        :param plaatsen: De nieuwe waarde van plaatsen; positieve integer
        :return: None
        post: De waarde van plaatsen is geüpdatet naar de gegeven value.
        """
        self.plaatsen_ = plaatsen


