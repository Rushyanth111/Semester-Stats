from .scheme_2015 import scheme_2015, total_scheme_2015
from .scheme_2017 import scheme_2017, total_scheme_2017


def process_marks(Scheme: int, Internal: int, External: int):
    if Scheme == 2010:
        pass
    if Scheme == 2015:
        return scheme_2015(Internal, External)
    if Scheme == 2017:
        return scheme_2017(Internal, External)


def total_process_marks(Scheme: int, Total: int):
    if Scheme == 2010:
        pass
    if Scheme == 2015:
        return total_scheme_2015(Total)
    if Scheme == 2017:
        return total_scheme_2017(Total)
