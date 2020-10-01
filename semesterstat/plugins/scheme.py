"""
Module Contains Plugins for FCD, FC, SC modifications.

"""

from typing import Any

from sqlalchemy import and_


def fcd(scheme: int, val: Any, compattr: Any):
    if scheme in (2015, 2017, 2018):
        return val >= (compattr * 0.7)
    else:
        return val >= (compattr * 0.7)


def fc(scheme: int, val: Any, compattr: Any):
    if scheme in (2015, 2017, 2018):
        return and_(val >= compattr * 0.6, val < 0.7 * compattr)
    else:
        return and_(val >= compattr * 0.6, val < 0.7 * compattr)


def sc(scheme: int, val: Any, compattr: Any):
    if scheme in (2015, 2017, 2018):
        return and_(val >= compattr * 0.4, val < 0.6 * compattr)
    else:
        return and_(val >= compattr * 0.4, val < 0.6 * compattr)
