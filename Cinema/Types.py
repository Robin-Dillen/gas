from typing import TypeVar, NewType
from Cinema.BuildingBlocks import _Foundation, Film, Gebruiker, Reservatie, Vertoning, Zaal


_BuildingBlock = TypeVar("_BuildingBlock", bound=_Foundation)
_FilmType = NewType('_FilmType', Film)
_GebruikerType = NewType('_GebruikerType', Gebruiker)
_ReservatieType = NewType('_ReservatieType', Reservatie)
_VertoningType = NewType('_VertoningType', Vertoning)
_ZaalType = NewType('_ZaalType', Zaal)