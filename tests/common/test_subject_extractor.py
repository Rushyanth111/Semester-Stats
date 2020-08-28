import pytest

from semesterstat.common import (
    get_subject_dept,
    get_subject_scheme,
    get_subject_semester,
    is_subject_lab,
)


@pytest.mark.parametrize(
    ["query", "sem", "scheme", "dept", "lab"],
    [
        ("17CS41", 4, 2017, "CS", False),
        ("15MATDIP31", 3, 2015, "XX", False),
        ("18ECS84", 8, 2018, "EC", False),
        ("18ECMP68", 6, 2018, "EC", False),
        ("18ECL67", 6, 2018, "EC", True),
        ("15EC553", 5, 2015, "EC", False),
    ],
)
class TestSubjectExtractor:
    def test_semester(self, query, sem, scheme, dept, lab):
        assert get_subject_semester(query) == sem

    def test_scheme(self, query, sem, scheme, dept, lab):
        assert get_subject_scheme(query) == scheme

    def test_dept(self, query, sem, scheme, dept, lab):
        assert get_subject_dept(query) == dept

    def test_lab(self, query, sem, scheme, dept, lab):
        assert is_subject_lab(query) == lab
