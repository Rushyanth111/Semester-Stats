from .Scheme2015 import Scheme2015


def ProcessMarks(Scheme: int, Internal: int, External: int):
    if Scheme == 2010:
        pass
    if Scheme == 2015:
        return Scheme2015(Internal, External)
    if Scheme == 2017:
        pass

