def Scheme2015(Internals: int, Externals: int) -> tuple:
    # Tuple Returns like (isPass, Total, PassClass)
    SubjectTotal = Internals + Externals
    if Externals is None or Internals is None:
        return (False, SubjectTotal, "Failed")

    if SubjectTotal < 40:
        return (False, SubjectTotal, "Failed")

    if 40 <= SubjectTotal <= 60:
        return (True, SubjectTotal, "TCD")

    if 60 <= SubjectTotal <= 70:
        return (True, SubjectTotal, "SCD")

    if 70 <= SubjectTotal <= 100:
        return (True, SubjectTotal, "FCD")
