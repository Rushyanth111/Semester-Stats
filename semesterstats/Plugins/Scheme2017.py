def Scheme2017(Internals: int, Externals: int) -> tuple:
    # Tuple Returns like (isPass, Total, PassClass)
    SubjectTotal = Internals + Externals
    if Externals is None or Internals is None:
        return (False, SubjectTotal, "Failed")

    if SubjectTotal < 40:
        return (False, SubjectTotal, "Failed")

    if 40 <= SubjectTotal <= 60:
        return (True, SubjectTotal, "SC")

    if 60 <= SubjectTotal <= 70:
        return (True, SubjectTotal, "FC")

    if 70 <= SubjectTotal <= 100:
        return (True, SubjectTotal, "FCD")


def TotalScheme2017(Total: int) -> tuple:
    # Tuple returns like (isPass, Total)
    if Total < 360:
        return (False, "Failed")
    elif 360 <= Total < 480:
        return (True, "SC")
    elif 480 <= Total < 560:
        return (True, "FC")
    else:
        return (True, "FCD")
