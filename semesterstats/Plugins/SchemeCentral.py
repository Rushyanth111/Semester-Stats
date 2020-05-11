from .Scheme2015 import Scheme2015
from .Scheme2017 import Scheme2017


def ProcessMarks(Scheme: int, Internal: int, External: int):
    if Scheme == 2010:
        pass
    if Scheme == 2015:
        return Scheme2015(Internal, External)
    if Scheme == 2017:
        return Scheme2017(Internal, External)
